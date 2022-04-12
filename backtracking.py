class Robot(self, grid_size):
  def clean_room_backtrack(candidate):
    if self.is_dirty(candidate):
      self.clean(candidate)
      return
    for next_candidate in self.cardinal_tiles:
      if self.is_valid(next_candidate):
        self.place(next_candidate)
        self.backtrack(next_candidate)
        self.remove(next_candidate)
  
  def is_dirty(candidate):
    # lookup candidate on history table
    pass
  
  def clean(candidate):
    # spray some soap and move the brush around
    pass

  def is_valid(candidate):
    # check if obstacle
    # check if cleaned
    pass

  def place(candidate):
    # candidate is [0, 1, 2, 3] meaning N, E, S, W
    # store in memory that it is covering this box
    # orient to candidate
    # hit the gas pedal 1 square
    pass

  def remove(candidate):
    # go back??
    pass




  pass
def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
