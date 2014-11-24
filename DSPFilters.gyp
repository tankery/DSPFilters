{

    'targets': [
        {
            'target_name': 'DSPFilters',
            'type': '<(component)',

            'include_dirs':[
                'shared/DSPFilters/include',
                'shared/DSPFilters/source',
            ],

            'sources': [
                '<!@(ls shared/DSPFilters/source/*.cpp)',
            ],

            'direct_dependent_settings': {
                'include_dirs':[
                    'shared/DSPFilters/include',
                ],

                'conditions': [
                    ['OS=="android"', {
                        'defines': [
                            'ST_NO_EXCEPTION_HANDLING',
                        ],
                    }],
                    ['OS=="ios"', {
                        'defines': [
                            'ST_NO_EXCEPTION_HANDLING',
                        ],
                    }],
                ],   # conditions
            },

            'conditions': [
                ['OS=="android"', {
                    'defines': [
                        'ST_NO_EXCEPTION_HANDLING',
                    ],
                }],
                ['OS=="ios"', {
                    'defines': [
                        'ST_NO_EXCEPTION_HANDLING',
                    ],
                }],
            ],   # conditions

        },
    ],

}
