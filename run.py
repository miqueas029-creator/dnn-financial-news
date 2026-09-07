import uvicorn
import sys
import os

if __name__ == "__main__":
    # Ensure current directory is in sys.path
    sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))
    print("=" * 65)
    print(" Starting DNN Financial News - Personalized Investor Feed")
    print(" Local Web URL:    http://localhost:8000")
    print(" Network Web URL:  http://0.0.0.0:8000 (accessible on same Wi-Fi)")
    print(" Interactive Docs: http://localhost:8000/docs")
    print("=" * 65)
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
