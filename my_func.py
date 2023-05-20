from manim import *
def next_dl(
    self,
    mobject_or_point,
    direction=DOWN,
    buff=DEFAULT_MOBJECT_TO_MOBJECT_BUFFER,
    aligned_edge=LEFT,
    submobject_to_align=None,
    index_of_submobject_to_align=None,
    coor_mask=np.array([1, 1, 1]),
):
    
    if isinstance(mobject_or_point, Mobject):
        mob = mobject_or_point
        if index_of_submobject_to_align is not None:
            target_aligner = mob[index_of_submobject_to_align]
        else:
            target_aligner = mob
        target_point = target_aligner.get_critical_point(aligned_edge + direction)
    else:
        target_point = mobject_or_point
    if submobject_to_align is not None:
        aligner = submobject_to_align
    elif index_of_submobject_to_align is not None:
        aligner = self[index_of_submobject_to_align]
    else:
        aligner = self
    point_to_align = aligner.get_critical_point(aligned_edge - direction)
    self.shift((target_point - point_to_align + buff * direction) * coor_mask)
    return self
Mobject.next_dl = next_dl
class MultiPlay(Scene):
    def multi_play(self,ani,wait_time=False,tim=None,time_value=1):
        if tim == None:
            tim = [time_value]*len(ani)
        for i in range(len(ani)):
            if ani[i][0]=='a':
                self.add(*ani[i][1:])
            elif ani[i][0]=='r':
                self.remove(*ani[i][1:])
            elif ani[i][0]=='m':
                ani[i][1:]
            else:
                self.play(*ani[i][:])
            
            if wait_time:
                if tim[i]>0:
                    self.wait(tim[i]) 
            else:
                pass