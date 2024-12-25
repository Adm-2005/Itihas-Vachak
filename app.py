from src.ui.gradio_interface import interface
from src.extraction import extract_and_clean

def main():
    extract_and_clean()
    interface.launch()

if __name__ == "__main__":
    main()