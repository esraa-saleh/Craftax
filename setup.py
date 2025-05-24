from setuptools import setup, find_packages

setup(
    name="craftax",
    version="1.4.5",
    author="Michael Matthews",
    author_email="michael.matthews@eng.ox.ac.uk",
    description="An open-world environment for training RL agents",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/MichaelTMatthews/Craftax",
    packages=find_packages(include=["craftax*"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "jax",
        "distrax",
        "optax",
        "flax",
        "numpy",
        "pygame",
        "gymnax",
        "chex",
        "matplotlib",
        "imageio",
    ],
    extras_require={
        "dev": [
            "black",
            "pre-commit",
        ],
    },
    entry_points={
        "console_scripts": [
            "play_craftax=craftax.craftax.play_craftax:entry_point",
            "play_craftax_classic=craftax.craftax_classic.play_craftax_classic:entry_point",
        ],
    },
)
