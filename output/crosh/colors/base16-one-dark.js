// Base16 One Dark
// Scheme: Base24

var color_scheme = {
        'base00': '#282c34',
        'base01': '#3f4451',
        'base02': '#4f5666',
        'base03': '#545862',
        'base04': '#9196a1',
        'base05': '#abb2bf',
        'base06': '#e6e6e6',
        'base07': '#ffffff',
        'base08': '#e06c75',
        'base09': '#d19a66',
        'base0A': '#e5c07b',
        'base0B': '#98c379',
        'base0C': '#56b6c2',
        'base0D': '#61afef',
        'base0E': '#c678dd',
        'base0F': '#be5046',
};

term_.prefs_.set('background-color', color_scheme.base00);
term_.prefs_.set('foreground-color', color_scheme.base05);
term_.prefs_.set('cursor-color', "rgba(171, 178, 191, 0.5)");

term_.prefs_.set('color-palette-overrides', 
                        [color_scheme.base00,
                        color_scheme.base08,
                        color_scheme.base0B,
                        color_scheme.base0A,
                        color_scheme.base0D,
                        color_scheme.base0E,
                        color_scheme.base0C,
                        color_scheme.base05,
                        color_scheme.base03,
                        color_scheme.base08,
                        color_scheme.base0B,
                        color_scheme.base0A,
                        color_scheme.base0D,
                        color_scheme.base0E,
                        color_scheme.base0C,
                        color_scheme.base07,
                        color_scheme.base09,
                        color_scheme.base0F,
                        color_scheme.base01,
                        color_scheme.base02,
                        color_scheme.base04,
                        color_scheme.base06]);
