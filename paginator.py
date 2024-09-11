from flask import request 

class Paginator:
  """docstring for Paginator"""
  def __init__(self, item_per_page):
    self.item_per_page = item_per_page
  
  @staticmethod
  def retrieve_page():
    return request.args.get("page", 1, type=int)

  def compute_bounds(self):
    start = ( self.retrieve_page() - 1 ) * self.item_per_page
    end = start + self.item_per_page
    return ( start, end )

  def extract_data(self, dataframe):
    start, *_ , end = self.compute_bounds()
    return dataframe[start:end]

  def has_next(self, dataframe):
    end = self.compute_bounds()
    return end[-1] < len(dataframe)

  def has_previous(self):
    start = self.compute_bounds()
    return start[0] > 0 