print("✅ Verifying your Python environment...\n")

try:
    import numpy
    print(f"✅ NumPy installed, version: {numpy.__version__}")
except ImportError:
    print("❌ NumPy not installed!")

try:
    import pandas
    print(f"✅ Pandas installed, version: {pandas.__version__}")
except ImportError:
    print("❌ Pandas not installed!")

try:
    import matplotlib
    print(f"✅ Matplotlib installed, version: {matplotlib.__version__}")
except ImportError:
    print("❌ Matplotlib not installed!")

try:
    import seaborn
    print(f"✅ Seaborn installed, version: {seaborn.__version__}")
except ImportError:
    print("❌ Seaborn not installed!")

try:
    import sklearn
    print(f"✅ scikit-learn installed, version: {sklearn.__version__}")
except ImportError:
    print("❌ scikit-learn not installed!")

print("\n🎉 Verification finished!")
