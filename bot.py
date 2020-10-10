from config import discord_client, DISCORD_TOKEN


def main():
    cogs = [
        "cogs.Basic"
    ]
    for ext in cogs:
        print(f"Loading {ext}...")
        discord_client.load_extension(ext)

    discord_client.run(DISCORD_TOKEN)


if __name__ == '__main__':
    main()
