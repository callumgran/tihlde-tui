import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.ui import TIHLDEApp

def main():
    TIHLDEApp().run()

if __name__ == "__main__":
    main()
