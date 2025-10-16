from django.conf import settings 
from omdb.client import OmdbClient


def get_client_from_settings():
  """Create an instance of an OMdbClient 
  using the OMDB_KEY from the Django settings """
  return OmdbClient(settings.OMDB_KEY)