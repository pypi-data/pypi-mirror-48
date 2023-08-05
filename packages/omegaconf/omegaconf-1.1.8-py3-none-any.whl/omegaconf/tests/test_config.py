"""Testing for OmegaConf"""
import os
import sys
import tempfile
import copy
import pytest
from pytest import raises
import random

from omegaconf import MissingMandatoryValue
from omegaconf import OmegaConf


def test_value():
    """Test a simple value"""
    s = 'hello'
    c = OmegaConf.create(s)
    assert {'hello': None} == c


def test_key_value():
    """Test a simple key:value"""
    s = 'hello: world'
    c = OmegaConf.create(s)
    assert {'hello': 'world'} == c


def test_key_map():
    """Test a key to map"""
    s = '{hello: {a : 2}}'
    c = OmegaConf.create(s)
    assert {'hello': {'a': 2}} == c


def test_empty_input():
    """Test empty input"""
    s = ''
    c = OmegaConf.create(s)
    assert c == {}


def test_setattr_value():
    c = OmegaConf.create('a: {b : {c: 1}}')
    c.a = 9
    assert {'a': 9} == c


def test_setattr_deep_value():
    c = OmegaConf.create('a: {b : {c: 1}}')
    c.a.b = 9
    assert {'a': {'b': 9}} == c


def test_setattr_deep_from_empty():
    c = OmegaConf.create()
    # Unfortunately we can't just do c.a.b = 9 here.
    # The reason is that if c.a is being resolved first and it does not exist, so there
    # is nothing to call .b = 9 on.
    # The alternative is to auto-create fields as they are being accessed, but this is opening
    # a whole new can of worms, and is also breaking map semantics.
    c.a = {}
    c.a.b = 9
    assert {'a': {'b': 9}} == c


def test_setattr_deep_map():
    c = OmegaConf.create('a: {b : {c: 1}}')
    c.a.b = {'z': 10}
    assert {'a': {'b': {'z': 10}}} == c





def test_dir():
    c = OmegaConf.create('a: b')
    assert ['a'] == dir(c)


def test_getattr():
    c = OmegaConf.create('a: b')
    assert 'b' == c.a


def test_getattr_dict():
    c = OmegaConf.create('a: {b: 1}')
    assert {'b': 1} == c.a


def test_str():
    c = OmegaConf.create('a: b')
    assert "{'a': 'b'}" == str(c)


def test_repr():
    c = OmegaConf.create('a: b')
    assert "{'a': 'b'}" == repr(c)


def test_is_empty_dict():
    c = OmegaConf.create('a: b')
    assert not c.is_empty()
    c = OmegaConf.create()
    assert c.is_empty()


def test_is_empty_list():
    c = OmegaConf.create('[1,2,3]')
    assert not c.is_empty()
    c = OmegaConf.create([])
    assert c.is_empty()


def test_list_value():
    c = OmegaConf.create('a: [1,2]')
    assert {'a': [1, 2]} == c


def test_tupple_value():
    c = OmegaConf.create((1, 2))
    assert (1, 2) == c


def test_list_of_dicts():
    v = dict(
        list=[
            dict(key1='value1'),
            dict(key2='value2')
        ])
    c = OmegaConf.create(v)
    assert c.list[0].key1 == 'value1'
    assert c.list[1].key2 == 'value2'


def test_from_file():
    with tempfile.NamedTemporaryFile() as fp:
        s = b'a: b'
        fp.write(s)
        fp.flush()
        fp.seek(0)
        c = OmegaConf.load(fp.file)
        assert {'a': 'b'} == c


def test_from_filename():
    # note that delete=False here is a work around windows incompetence.
    try:
        with tempfile.NamedTemporaryFile(delete=False) as fp:
            s = b'a: b'
            fp.write(s)
            fp.flush()
            c = OmegaConf.load(fp.name)
            assert {'a': 'b'} == c
    finally:
        os.unlink(fp.name)


def test_from_dict1():
    d = {'a': 2, 'b': 10}
    c = OmegaConf.create(d)
    assert d == c


def test_from_dict2():
    d = dict(a=2, b=10)
    c = OmegaConf.create(d)
    assert d == c


def test_from_nested_dict():
    d = {'a': 2, 'b': {'c': {'f': 1}, 'd': {}}}
    c = OmegaConf.create(d)
    assert d == c


def test_cli_config():
    sys.argv = ['program.py', 'a=1', 'b.c=2']
    c = OmegaConf.from_cli()
    assert {'a': 1, 'b': {'c': 2}} == c


def test_cli_passing():
    args_list = ['a=1', 'b.c=2']
    c = OmegaConf.from_cli(args_list)
    assert {'a': 1, 'b': {'c': 2}} == c


def test_mandatory_value():
    c = OmegaConf.create('{a: "???"}')
    with raises(MissingMandatoryValue):
        c.get('a')


def test_subscript_get():
    c = OmegaConf.create('a: b')
    assert 'b' == c['a']


def test_subscript_set():
    c = OmegaConf.create()
    c['a'] = 'b'
    assert {'a': 'b'} == c


def test_pretty_dict():
    c = OmegaConf.create(dict(
        hello='world',
        list=[
            1,
            2
        ]
    ))
    expected = '''hello: world
list:
- 1
- 2
'''
    assert expected == c.pretty()


def test_pretty_list():
    c = OmegaConf.create([
        'item1',
        'item2',
        dict(key3='value3')
    ])
    expected = '''- item1
- item2
- key3: value3
'''
    assert expected == c.pretty()


def test_scientific_number():
    c = OmegaConf.create('a: 10e-3')
    assert 10e-3 == c.a


def test_with_default():
    s = '{hello: {a : 2}}'
    c = OmegaConf.create(s)
    assert c.get('missing', 4) == 4
    assert c.hello.get('missing', 5) == 5
    assert {'hello': {'a': 2}} == c


def test_map_expansion():
    c = OmegaConf.create('{a: 2, b: 10}')

    def foo(a, b):
        return a + b

    assert 12 == foo(**c)


def test_items():
    c = OmegaConf.create('{a: 2, b: 10}')
    assert {'a': 2, 'b': 10}.items() == c.items()


def test_pickle():
    with tempfile.TemporaryFile() as fp:
        s = 'a: b'
        import pickle
        c = OmegaConf.create(s)
        pickle.dump(c, fp)
        fp.flush()
        fp.seek(0)
        c1 = pickle.load(fp)
        assert c == c1


def test_pickle_get_root():
    # Test that get_root() is reconstructed correctly for pickle loaded files.
    with tempfile.TemporaryFile() as fp:
        c1 = OmegaConf.create(dict(
            a=dict(
                a1=1,
                a2=2,
            ),
        ))

        c2 = OmegaConf.create(dict(
            b=dict(
                b1='???',
                b2=4,
                bb=dict(
                    bb1=3,
                    bb2=4,
                ),
            ),
        ))
        c3 = OmegaConf.merge(c1, c2)

        import pickle
        pickle.dump(c3, fp)
        fp.flush()
        fp.seek(0)
        loaded_c3 = pickle.load(fp)

        def test(conf):
            assert conf._get_root() == conf
            assert conf.a._get_root() == conf
            assert conf.b._get_root() == conf
            assert conf.b.bb._get_root() == conf

        assert c3 == loaded_c3
        test(c3)
        test(loaded_c3)


def test_iterate_dictionary():
    c = OmegaConf.create('''
    a : 1
    b : 2
    ''')
    m2 = {}
    for key in c:
        m2[key] = c[key]
    assert m2 == c


def test_iterate_list():
    c = OmegaConf.create([1, 2])
    items = [x for x in c]
    assert items[0] == 1
    assert items[1] == 2


def test_items():
    c = OmegaConf.create('''
    a:
      v: 1
    b:
      v: 1
    ''')
    for k, v in c.items():
        v.v = 2

    assert c.a.v == 2
    assert c.b.v == 2


def test_pop():
    c = OmegaConf.create('''
    a : 1
    b : 2
    ''')
    assert 1 == c.pop('a')
    assert {'b': 2} == c


def test_merge_from_1():
    a = OmegaConf.create()
    b = OmegaConf.create('''
    a : 1
    b : 2
    ''')
    a.merge_from(b)
    assert a == b


def test_merge_from_2():
    a = OmegaConf.create()
    a.inner = {}
    b = OmegaConf.create('''
    a : 1
    b : 2
    ''')
    a.inner.merge_from(b)
    assert a.inner == b


def test_nested_map_merge_bug():
    cfg = """
launcher:
  queue: a
  queues:
    local:
      clazz: foo

"""
    cli = """
launcher:
  instances: 2
"""
    cfg = OmegaConf.create(cfg)
    cli = OmegaConf.create(cli)
    ret = OmegaConf.merge(cfg, cli)
    assert ret.launcher.queues is not None


def test_in_dict():
    c = OmegaConf.create(dict(
        a=1,
        b=2,
        c={}))
    assert 'a' in c
    assert 'b' in c
    assert 'c' in c
    assert 'd' not in c


def test_in_list():
    c = OmegaConf.create([10, 11, dict(a=12)])
    assert 10 in c
    assert 11 in c
    assert dict(a=12) in c
    assert 'blah' not in c


def test_get_root():
    c = OmegaConf.create(dict(
        a=123,
        b=dict(
            bb=456,
            cc=7,
        ),
    ))
    assert c._get_root() == c
    assert c.b._get_root() == c


def test_get_root_of_merged():
    c1 = OmegaConf.create(dict(
        a=dict(
            a1=1,
            a2=2,
        ),
    ))

    c2 = OmegaConf.create(dict(
        b=dict(
            b1='???',
            b2=4,
            bb=dict(
                bb1=3,
                bb2=4,
            ),
        ),
    ))
    c3 = OmegaConf.merge(c1, c2)

    assert c3._get_root() == c3
    assert c3.a._get_root() == c3
    assert c3.b._get_root() == c3
    assert c3.b.bb._get_root() == c3


def test_str_interpolation_1():
    # Simplest str_interpolation
    c = OmegaConf.create(dict(
        a='${referenced}',
        referenced='bar',
    ))
    assert c.referenced == 'bar'
    assert c.a == 'bar'


def test_str_interpolation_key_error_1():
    # Test that a KeyError is thrown if an str_interpolation key is not available
    c = OmegaConf.create(dict(
        a='${not_found}',
    ))

    with pytest.raises(KeyError):
        c.a


def test_str_interpolation_key_error_2():
    # Test that a KeyError is thrown if an str_interpolation key is not available
    c = OmegaConf.create(dict(
        a='${not.found}',
    ))

    with pytest.raises(KeyError):
        c.a


def test_str_interpolation_3():
    # Test that str_interpolation works with complex strings
    c = OmegaConf.create(dict(
        a='the year ${year}',
        year='of the cat',
    ))

    assert c.a == 'the year of the cat'


def test_str_interpolation_4():
    # Test that a string with multiple str_interpolations works
    c = OmegaConf.create(dict(
        a='${ha} ${ha} ${ha}, said Pennywise, ${ha} ${ha}... ${ha}!',
        ha='HA',
    ))

    assert c.a == 'HA HA HA, said Pennywise, HA HA... HA!'


def test_deep_str_interpolation_1():
    # Test deep str_interpolation works
    c = OmegaConf.create(dict(
        a='the answer to the universe and everything is ${nested.value}',
        nested=dict(
            value=42
        ),
    ))

    assert c.a == 'the answer to the universe and everything is 42'


def test_deep_str_interpolation_2():
    # Test that str_interpolation of a key that is nested works
    c = OmegaConf.create(dict(
        out=42,
        deep=dict(
            inside='the answer to the universe and everything is ${out}',
        ),
    ))

    assert c.deep.inside == 'the answer to the universe and everything is 42'


def test_simple_str_interpolation_inherit_type():
    # Test that str_interpolation of a key that is nested works
    c = OmegaConf.create(dict(
        inter1='${answer1}',
        inter2='${answer2}',
        inter3='${answer3}',
        inter4='${answer4}',
        answer1=42,
        answer2=42.0,
        answer3=False,
        answer4='string',
    ))

    assert type(c.inter1) == int
    assert type(c.inter2) == float
    assert type(c.inter3) == bool
    assert type(c.inter4) == str


def test_complex_str_interpolation_is_always_str_1():
    c = OmegaConf.create(dict(
        two=2,
        four=4,
        inter1='${four}${two}',
        inter2='4${two}',
    ))

    assert type(c.inter1) == str
    assert c.inter1 == '42'
    assert type(c.inter2) == str
    assert c.inter2 == '42'


def test_interpolation_fails_on_config():
    # Test that a ValueError is thrown if an string interpolation used on config value
    c = OmegaConf.create(dict(
        config_obj=dict(
            value1=42,
            value2=43,
        ),
        deep=dict(
            inside='${config_obj}',
        ),
    ))

    with pytest.raises(ValueError):
        c.deep.inside


def test_2_step_interpolation():
    c = OmegaConf.create(dict(
        src='bar',
        copy_src='${src}',
        copy_copy='${copy_src}',
    ))
    assert c.copy_src == 'bar'
    assert c.copy_copy == 'bar'


def test_env_interpolation1():
    try:
        os.environ['foobar'] = '1234'
        c = OmegaConf.create(dict(
            path='/test/${env:foobar}',
        ))
        assert c.path == '/test/1234'
    finally:
        del os.environ['foobar']
        OmegaConf.clear_resolvers()


def test_env_interpolation_not_found():
    c = OmegaConf.create(dict(
        path='/test/${env:foobar}',
    ))
    with pytest.raises(KeyError):
        c.path


def test_env_interpolation_recursive1():
    c = OmegaConf.create(dict(
        path='/test/${path}',
    ))

    with pytest.raises(RuntimeError):
        c.path


def test_env_interpolation_recursive2():
    c = OmegaConf.create(dict(
        path1='/test/${path2}',
        path2='/test/${path1}',
    ))

    with pytest.raises(RuntimeError):
        c.path1


def test_deepcopy():
    c1 = OmegaConf.create(dict(
        foo1='foo1',
        foo2='foo2',
    ))

    c2 = copy.deepcopy(c1)
    assert c2 == c1
    c1.foo1 = "bar"
    assert c1.foo1 == 'bar'
    assert c2.foo1 == 'foo1'


def test_register_resolver_twice_error():
    try:
        OmegaConf.register_resolver("foo", lambda: 10)
        with pytest.raises(AssertionError):
            OmegaConf.register_resolver("foo", lambda: 10)
    finally:
        OmegaConf.clear_resolvers()


def test_clear_resolvers():
    assert OmegaConf.get_resolver('foo') is None
    try:
        OmegaConf.register_resolver('foo', lambda x: int(x) + 10)
        assert OmegaConf.get_resolver('foo') is not None
    finally:
        OmegaConf.clear_resolvers()
        assert OmegaConf.get_resolver('foo') is None


def test_register_resolver_1():
    try:
        OmegaConf.register_resolver("plus_10", lambda x: int(x) + 10)
        c = OmegaConf.create(dict(
            k='${plus_10:990}',
        ))

        assert type(c.k) == int
        assert c.k == 1000
    finally:
        OmegaConf.clear_resolvers()


def test_register_resolver_2():
    # resolvers are always converted to stateless idempotent functions
    # subsequent calls to the same function with the same argument will always return the same value.
    # this is important to allow embedding of functions like time() without having the value change during
    # the program execution.
    try:
        OmegaConf.register_resolver("random", lambda _: random.randint(0, 10000000))
        c = OmegaConf.create(dict(
            k='${random:_}',
        ))
        assert c.k == c.k
    finally:
        OmegaConf.clear_resolvers()


def test_is_dict():
    c = OmegaConf.create(dict())
    assert c.is_dict()
    assert not c.is_sequence()


def test_is_sequence_with_list():
    c = OmegaConf.create([])
    assert not c.is_dict()
    assert c.is_sequence()


def test_is_sequence_with_tupple():
    c = OmegaConf.create(())
    assert not c.is_dict()
    assert c.is_sequence()


def test_items_on_list():
    c = OmegaConf.create([1, 2])
    with raises(TypeError):
        c.items()


def test_merge_list_root():
    c1 = OmegaConf.create([1, 2, 3])
    c2 = OmegaConf.create([4, 5, 6])
    c3 = OmegaConf.merge(c1, c2)
    assert c3 == [1, 2, 3, 4, 5, 6]


def test_merge_tuple_root():
    c1 = OmegaConf.create((1, 2, 3))
    c2 = OmegaConf.create((4, 5, 6))
    c3 = OmegaConf.merge(c1, c2)
    assert c3 == [1, 2, 3, 4, 5, 6]


def test_merge_list_nested_in_list():
    c1 = OmegaConf.create([[1, 2, 3]])
    c2 = OmegaConf.create([[4, 5, 6]])
    c3 = OmegaConf.merge(c1, c2)
    assert c3 == [[1, 2, 3], [4, 5, 6]]


def test_merge_list_nested_in_dict():
    c1 = OmegaConf.create(dict(list=[1, 2, 3]))
    c2 = OmegaConf.create(dict(list=[4, 5, 6]))
    c3 = OmegaConf.merge(c1, c2)
    assert c3 == dict(list=[1, 2, 3, 4, 5, 6])


def test_merge_dict_nested_in_list():
    c1 = OmegaConf.create([1, 2, dict(a=10)])
    c2 = OmegaConf.create([4, 5, dict(b=20)])
    c3 = OmegaConf.merge(c1, c2)
    assert c3 == [1, 2, dict(a=10), 4, 5, dict(b=20)]
