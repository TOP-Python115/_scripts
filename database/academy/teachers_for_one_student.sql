select 
	concat(s.name, ' ', s.surname) as `Student`,
    concat(t.name, ' ', t.surname) as `Teacher`
  from students as s
  join groupsstudents as gs
    on gs.studentid = s.id
  join `groups` as g
    on gs.groupid = g.id
  join groupslectures as gl
    on gl.groupid = g.id
  join lectures as l
    on gl.lectureid = l.id
  join teachers as t
    on t.id = l.teacherid
where s.id = 14
