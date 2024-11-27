from gftools.builder.recipeproviders.googlefonts import GFBuilder

# Taken from gftools-builder
DEFAULTS = {
    "outputDir": "../fonts",
    "vfDir": "$outputDir/variable",
    "ttDir": "$outputDir/ttf",
    "otDir": "$outputDir/otf",
    "woffDir": "$outputDir/webfonts",
    "buildVariable": True,
    "buildStatic": False,
    "buildOTF": False,
    "buildTTF": False,
    "buildSmallCap": False,
    "buildWebfont": False,
    "autohintTTF": True,
    "autohintOTF": False,
    "ttfaUseScript": True,
    "logLevel": "WARN",
    "cleanUp": True,
    "includeSourceFixes": False,
    "fvarInstanceAxisDflts": None,
    "flattenComponents": True,
    "addGftoolsVersion": True,
    "decomposeTransformedComponents": True,
    "interpolate": False,
    "useMutatorMath": False,
    "checkCompatibility": True,
    "overlaps": "booleanOperations",
    "splitItalic": True,
}

class InterExtensionBuilder(GFBuilder):
    def write_recipe(self):
        self.config = {**DEFAULTS, **self.config}
        recipe = super(InterExtensionBuilder, self).write_recipe()
        return recipe
        
    