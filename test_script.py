Dict={
    "name":"talha",
    "skills":["python","sql","django","llm"]
}
str=''''
<table>
{% for item in items %}
<TR>
   <TD class="c1"><IMG src="favicon.ico"></TD>
   <TD class="c2">{{item.date}}</TD>
   <TD class="c3">{{item.id}}</TD>
   <TD class="c4"><SPAN>{{item.position}}</SPAN></TD>
   <TD class="c5"><SPAN>{{item.status}}</SPAN></TD>
</TR>
{% endfor %}
</table>




'''
