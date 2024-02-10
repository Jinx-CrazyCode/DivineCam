from setuptools import setup

setup(
    name="DivineCam",
    version="1.0",
    description="this library is to simplify the OpenCV library",
    url="https://github.com/Jinx-CrazyCode/DivineCam",
    license="MIT",
    author="Rose Divine",
    keywords="python, cv, opencv, CCTV, cctv, IPCAM, IP-CAM, ipcam, ip-cam",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
    ],
    install_requires=["opencv-python"],
    packages=["Camera.py"],
)
