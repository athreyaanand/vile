from Universe import Universe

universe = Universe()
universe.spawn(["adam", "eve"])

universe.run(5)
universe.run(3)
universe.run(2)

universe.end()