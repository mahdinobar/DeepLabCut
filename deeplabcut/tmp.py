import deeplabcut

if __name__ == "__main__":
    deeplabcut.evaluate_network('/media/mahdi/LaCie/Mahdi/DLC/projects/project_1/VV2Dpose-mahdi-2/ config.yaml',Shuffles=[1], plotting=True, show_errors=True)

    print('end')