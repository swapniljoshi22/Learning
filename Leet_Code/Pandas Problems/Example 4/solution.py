import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    result = teacher.groupby(['teacher_id']).agg(
    cnt=pd.NamedAgg(column='subject_id', aggfunc='nunique')).reset_index()
    return result