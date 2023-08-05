import re, enum
from datetime import datetime, timedelta
from collections import namedtuple
import yaml
import json
from pathlib import Path


class Diary:
    def __init__(self, hyperdiary_json):
        for key, val in hyperdiary_json.items():
            setattr(self, key, val)
        if not hasattr(self, 'expected'):
            self.expected = expected
        self.expected = [DateRange.from_json(obj) for obj in self.expected]
        self.entries = None
    
    def load_entries(self):
        self.entries = dict()
        for fname in self.sources:
            with open(fname) as f:
                for dt, entry in yaml.load(f, Loader=yaml.SafeLoader).items():
                    if dt in self.entries:
                        raise Exception('Double definition for {0} in file {1}'.format(dt, fname))
                    self.entries[dt] = entry
    
    @staticmethod
    def discover(path):
        path = Path(path).resolve()
        while not (path / 'hyperdiary.json').exists() and len(path.parts) > 1:
            path = path.parent
        hyperdiary_json_path = path / 'hyperdiary.json'
        if not hyperdiary_json_path.exists():
            raise FileNotFoundError('No hyperdiary.json found in any parent directories')
        with open(str(hyperdiary_json_path), 'r') as f:
            hyperdiary_json = json.load(f)
            hyperdiary_json['sources'] = [str(path / f) for f in hyperdiary_json['sources']]
            return Diary(hyperdiary_json)
    
    @staticmethod
    def discover_and_load(path='.'):
        diary = Diary.discover(path)
        diary.load_entries()
        return diary


class DateRange:
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __iter__(self):
        current = self.start
        one_day = timedelta(days=1)
        while current <= self.end:
            yield current
            current += one_day
    
    @staticmethod
    def from_json(obj):
        if not 'start' in obj:
            raise KeyError('"start" is required in an expected date range')
        start = datetime.strptime(obj['start'], '%Y-%m-%d').date()
        if 'end' in obj:
            end = datetime.strptime(obj['end'], '%Y-%m-%d').date()
        else:
            end = datetime.today().date()
        return DateRange(start, end)


@enum.unique
class EntryType(enum.Enum):
    Line = 1
    Dict = 2
    DictLine = 3


def iter_entries(yml):
    for date, entries in yml.items():
        #date = datetime.strptime(date, '%Y-%m-%d').date() not required, apperently already parsed to date object
        for entry in entries:
            if isinstance(entry, str):
                yield (date, entry, EntryType.Line)
            elif isinstance(entry, dict):
                for k, v in entry.items():
                    yield (date, k, EntryType.Dict)
                    for l in v:
                        yield (date, l, EntryType.DictLine)


def find_tags(line):
    '''
    >>> res = [t.text for t in find_tags("+tag1 +tag2 some content goes here +tag3")]
    >>> res == ["tag1", "tag2", "tag3"]
    True
    '''
    return find(line, TokenType.Tag)


def find_ids(line):
    return find(line, TokenType.Id)


def find(line, token_type):
    return [token for token in tokenize(line) if token.type == token_type]


@enum.unique
class TokenType(enum.Enum):
    Text = 1
    Tag = 2
    Id = 3


_REPLACEMENTS = {
    '&': 'and',
    'ä': 'ae',
    'ö': 'oe',
    'ü': 'ue',
    'ß': 'ss',
    '\'': ''
}


def make_id(sid):
    sid = sid.lower()
    for k, v in _REPLACEMENTS.items():
        sid = sid.replace(k, v)
    assert not ' ' in sid, sid
    return sid


def _capitalize(s):
    up = True
    for l in s:
        if up:
            yield l.upper()
            up = False
        else:
            if l == ' ':
                up = True
            yield l


def beautify_id(sid):
    return ''.join(_capitalize(sid.replace('_', ' ')))


class Token:
    def __init__(self, type, text, ref=None):
        self.type = type
        self.text = text
        self.ref = ref
        if type == TokenType.Id:
            if not ref:
                s = text.split('|', 1)
                self.text = beautify_id( s[1] if len(s)==2 else s[0] )
                self.ref = make_id(s[0])

    def __repr__(self):
        return 'Token({0}, "{1}", "{2}")'.format(self.type, self.text, self.ref)

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False
        if self.type == TokenType.Id and other.type == TokenType.Id:
            return self.ref == other.ref
        return self.type == other.type and self.text == other.text and self.ref == other.ref

    def __hash__(self):
        if self.type == TokenType.Id:
            return hash(self.type) ^ hash(self.ref)
        return hash(self.type) ^ hash(self.text) ^ hash(self.ref)

    def __lt__(self, other):
        return self.text < other.text


re_separator = re.compile(' |;|,|\\.')


def _fragmented_tokenize(line):
    current = []
    current_type = TokenType.Text
    for l in line:
        if re_separator.match(l):
            if current:
                yield Token(current_type, ''.join(current))
            yield Token(TokenType.Text, l)
            current = []
            current_type = TokenType.Text
            continue
        if not current:
            if l == '+':
                current_type = TokenType.Tag
            elif l == '$':
                current_type = TokenType.Id
            else:
                current_type = TokenType.Text
            current.append(l if current_type == TokenType.Text else '')
            continue
        current.append(l)
    if current:
        yield Token(current_type, ''.join(current))


def tokenize(line):
    text_token = Token(TokenType.Text, '')
    for next in _fragmented_tokenize(line):
        if next.type == TokenType.Text:
            text_token = Token(TokenType.Text, text_token.text + next.text)
        else:
            if text_token.text:
                yield text_token
                text_token = Token(TokenType.Text, '')
            yield next
    if text_token.text:
        yield text_token
