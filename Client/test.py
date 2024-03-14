from chains_generator import RandomChainsGenerator

gen = RandomChainsGenerator(1000000)
gen.generate_chains()

for chain in gen.generated_chains:
    print(f"CHAIN: {chain}")
    print("len test\n")
    assert len(chain) >= 50 and len(chain) <= 100
    print("blanck spaces test\n")
    count = chain.count(' ')
    assert count in [3, 4, 5]
