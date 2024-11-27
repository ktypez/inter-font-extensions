import glob
import copy
import os

configs = glob.glob("sources/config-*.yaml")

for config in configs:
  with open(config, "r") as fs:
    txt = fs.read()
    replaced = txt.replace("recipeProvider: inter_extension", "recipeProvider: inter_extension_vf")
    
    new_file = "sources/vf-" + os.path.basename(config)
    with open(new_file, "w") as file:
      file.write(replaced)
      file.close()
    
    fs.close()
    