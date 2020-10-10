from .basic_cog import BasicCog


def setup(client):
    client.add_cog(BasicCog(client))