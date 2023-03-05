import json, datetime
from helper import datetimeNowFormatted

class Todo():
  def __init__(
      self,
      ID: str,
      Title: str,
      Description: str,
      FinishedAt: str | None,
      CreatedAt: str,
      UpdatedAt: str,
      DeletedAt: str | None
    ) -> None:
    self.ID = ID
    self.Title = Title
    self.Description = Description
    self.FinishedAt = FinishedAt
    self.CreatedAt = CreatedAt
    self.UpdatedAt = UpdatedAt
    self.DeletedAt = DeletedAt

  def toJSON(self) -> any:
    return json.loads(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4))

  def get_id(self) -> int:
    return self.ID
  
  def set_delete(self) -> None:
    now = datetimeNowFormatted()
    self.DeletedAt = now
    self.UpdatedAt = now

  def set_update(self, title = "", desctiption = "") -> None:
    now = datetimeNowFormatted()
    self.Title = title
    self.Description = desctiption
    self.UpdatedAt = now
  
  def set_finish(self) -> None:
    now = datetimeNowFormatted()
    self.FinishedAt = now
    self.UpdatedAt = now
  

  

  

    

