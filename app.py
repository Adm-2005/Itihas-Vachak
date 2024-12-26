from src.ui.gradio_interface import interface
from src.extraction import extract_and_clean

def main():
    # extract_and_clean() # All the processed files are included alongside the repository, thus removed raw files to reduce load time 
    interface.launch()

if __name__ == "__main__":
    main()