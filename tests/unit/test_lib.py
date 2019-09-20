#!/usr/bin/python3


class TestLib():
    def test_pytest(self):
        assert True

    def test_dansexample(self, dansexample):
        ''' See if the helper fixture works to load charm configs '''
        assert isinstance(dansexample.charm_config, dict)

    # Include tests for functions in lib_dans_example
