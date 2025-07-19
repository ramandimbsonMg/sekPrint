module.exports = {
    content: [
        '../templates/**/*.html',
        '../../templates/**/*.html',
        '../../**/templates/**/*.html',
    ],
    theme: {
        extend: {
            colors: {
                gray: {
                    100: '#f5f5f5', // Blanc cassé
                    200: '#e5e5e5', // Gris très clair
                    300: '#d4d4d4', // Gris clair
                    DEFAULT: '#a3a3a3', // Gris moyen (par défaut)
                    500: '#737373', // Gris un peu foncé
                    600: '#525252', // Gris foncé
                    700: '#404040', // Presque noir
                    800: '#262626',
                    900: '#171717',
                },
                secondary: {
                    100: '#cffafe', // Bleu très clair
                    200: '#a5f3fc',
                    300: '#67e8f9',
                    DEFAULT: '#22d3ee', // Bleu-vert (cyan doux)
                    500: '#06b6d4', // Cyan classique
                    600: '#0891b2',
                    700: '#0e7490',
                    800: '#155e75',
                    900: '#164e63',
                },
                // secondary: {
                //     100: '#fce7f3', // Rose très pâle
                //     200: '#fbcfe8',
                //     300: '#f9a8d4',
                //     DEFAULT: '#f472b6', // Rose vif
                //     500: '#ec4899',
                //     600: '#db2777',
                //     700: '#be185d',
                //     800: '#9d174d',
                //     900: '#831843',
                // },
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),
        require('@tailwindcss/aspect-ratio'),
    ],
}
