from pycgilib.environ import environ
class testeviron:
    def update_test(self):
        env = environ()
        env.update('test_var','test value')
        assert env.get('test_var') == 'test value'
        env.test_var2 = 'test value2'
        assert env.test_var2 == 'test value2'
    def remove_test(self):
        env = environ()
        assert env.test_var == 'test value'
        env.remove('test_var')
        assert 'test_var' not in env.environ
        env.test_var2 = 'test value2'
        del env.test_var2
        assert 'test_var' not in env.environ
