import os
import pathlib

def add_import(imports):
    with open(dir, "w") as new_file:
        if original_text != content:
            package_index = original_text.find('package')
            line_end_index = original_text.find('\n', package_index)

            modified_text = content[:line_end_index] + '\nimport ' + imports

            if name.endswith(".java"):
                modified_text += ";"
            modified_text += "\n" + content[line_end_index:]
            new_file.write(modified_text)
        else:
            new_file.write(content)


input("MAKE SURE YOU HAVE MADE A BACKUP OF YOUR PROJECT BEFORE RUNNING THIS SCRIPT (press enter to continue)\n")

try:
    os.chdir('src')
except FileNotFoundError:
    input('Please put this script next to the src/ directory! (press enter to exit)')
    exit()

for path, _, files in os.walk("."):
    for name in files:
        dir = str(pathlib.PurePath(path, name))
        if not (name.endswith(".java") or name.endswith(".kt")):
            continue

        with open(dir,"r+") as f:
            new_f = f.readlines()
            f.seek(0)
            for line in new_f:
                if "import gg.essential.universal" in line:
                    f.write(line.replace("gg.essential.universal", "cc.polyfrost.oneconfig.libs.universal"))
                elif "import gg.essential.elementa" in line:
                    f.write(line.replace("gg.essential.elementa", "cc.polyfrost.oneconfig.libs.elementa"))
                elif "import gg.essential.api" not in line:
                    f.write(line)
                
            f.truncate()

input("Finished removing Essential imports.\n\nPress enter to start replacing essential methods.\n")

for path, _, files in os.walk("."):
    for name in files:
        dir = str(pathlib.PurePath(path, name))
        if not (name.endswith(".java") or name.endswith(".kt")):
            continue

        with open(dir, "r") as file:
            original_text = file.read()
        with open(dir, "r+") as file:
            content = file.read().replace("EssentialAPI.getCommandRegistry().registerCommand", "CommandManager.INSTANCE.registerCommand").replace("EssentialAPI.getCommandRegistry().registerParser", "CommandManager.INSTANCE.addParser")
        add_import("cc.polyfrost.oneconfig.utils.commands.CommandManager")
   
        with open(dir, "r") as file:
            original_text = file.read()
        with open(dir, "r+") as file:
            content = file.read().replace("EssentialAPI.getNotifications().push", "Notifications.INSTANCE.send")
        add_import("cc.polyfrost.oneconfig.utils.Notifications")

        with open(dir, "r") as file:
            original_text = file.read()
        with open(dir, "r+") as file:
            content = file.read().replace("EssentialAPI.getGuiUtil().openScreen", "GuiUtils.displayScreen").replace("GuiUtil.openScreen", "GuiUtils.displayScreen")
        add_import("cc.polyfrost.oneconfig.utils.gui.GuiUtils")

        with open(dir, "r") as file:
            original_text = file.read()
        with open(dir, "r+") as file:
            content = file.read().replace("EssentialAPI.getGuiUtil().openedScreen", "UScreen.getCurrentScreen").replace("GuiUtil.openedScreen", "UScreen.getCurrentScreen")
        add_import("cc.polyfrost.oneconfig.libs.universal.UScreen")

        with open(dir, "r") as file:
            original_text = file.read()
        with open(dir, "r+") as file:
            content = file.read().replace("EssentialAPI.getMinecraftUtil().isHypixel", "HypixelUtils.INSTANCE.isHypixel")
        add_import("cc.polyfrost.oneconfig.utils.hypixel.HypixelUtils")

        with open(dir, "r") as file:
            original_text = file.read()
        with open(dir, "r+") as file:
            content = file.read().replace("EssentialAPI.getMinecraftUtil().sendMessage", "UChat.chat")
        add_import("cc.polyfrost.oneconfig.libs.universal.UChat")

        with open(dir, "r") as file:
            original_text = file.read()
        with open(dir, "r+") as file:
            content = file.read().replace("EssentialAPI.getShutdownHookUtil().register", "Runtime.getRuntime().addShutdownHook")

input("Done! (press enter to exit)")
