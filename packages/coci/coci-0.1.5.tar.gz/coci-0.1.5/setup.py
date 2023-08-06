from setuptools import setup

setup(
    name="coci",
    version="0.1.5",
    author="Koki Fujiwara",
    author_email="koki.fujiwara@exwzd.com",
    description="Collective Observation on Causal Inference",
    install_requires=["numpy", "seaborn"],
    packages=["coci"],
)