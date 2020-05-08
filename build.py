from cpt.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(settings={"arch": "x86_64"})
    builder.add_common_builds()
    builder.run()
