#@begin Linear_OR #@desc Linear OpenRefine Workflow
#@param expression:grel:value.replace(/[\\[\\]"";?()\\*!']/,'_')
#@param expression:grel:toString(toDate(value),"yyyy-MM-dd")
#@param col-name:event
#@param col-name:event_grouped
#@param col-name:notes
#@param col-name:physical_description
#@param expression:grel:value.replace(/[\\[\\];?()\\*!]/,'_')
#@param expression:value.toTitlecase()
#@param col-name:name
#@param col-name:currency
#@param col-name:venue
#@param col-name:call_number
#@param expression:value.toNumber()
#@param col-name:location
#@param col-name:place
#@param expression:grel:value.replace(/[\\[\\]"";?()\\*!]/,'_')
#@param col-name:page_count
#@param col-name:sponsor
#@param col-name:occasion
#@param expression:value.trim()
#@param col-name:status
#@param expression:value.replace(/\\s+/,'_')
#@param col-name:dish_count
#@param newColumnName:event_grouped
#@param expression:value.toDate()
#@param col-name:id
#@param col-name:date
#@in table0
#@out table132
#@begin core/text-transform0#@desc Text transform on cells in column name using expression value.trim()
#@param col-name:name
#@param expression:value.trim()
#@in table0
#@out table1
#@end core/text-transform0
#@begin core/text-transform1#@desc Text transform on cells in column sponsor using expression value.trim()
#@param col-name:sponsor
#@param expression:value.trim()
#@in table1
#@out table2
#@end core/text-transform1
#@begin core/text-transform2#@desc Text transform on cells in column event using expression value.trim()
#@param col-name:event
#@param expression:value.trim()
#@in table2
#@out table3
#@end core/text-transform2
#@begin core/text-transform3#@desc Text transform on cells in column venue using expression value.trim()
#@param col-name:venue
#@param expression:value.trim()
#@in table3
#@out table4
#@end core/text-transform3
#@begin core/text-transform4#@desc Text transform on cells in column physical_description using expression value.trim()
#@param col-name:physical_description
#@param expression:value.trim()
#@in table4
#@out table5
#@end core/text-transform4
#@begin core/text-transform5#@desc Text transform on cells in column venue using expression value.trim()
#@param col-name:venue
#@param expression:value.trim()
#@in table5
#@out table6
#@end core/text-transform5
#@begin core/text-transform6#@desc Text transform on cells in column place using expression value.trim()
#@param col-name:place
#@param expression:value.trim()
#@in table6
#@out table7
#@end core/text-transform6
#@begin core/text-transform7#@desc Text transform on cells in column physical_description using expression value.trim()
#@param col-name:physical_description
#@param expression:value.trim()
#@in table7
#@out table8
#@end core/text-transform7
#@begin core/text-transform8#@desc Text transform on cells in column occasion using expression value.trim()
#@param col-name:occasion
#@param expression:value.trim()
#@in table8
#@out table9
#@end core/text-transform8
#@begin core/text-transform9#@desc Text transform on cells in column notes using expression value.trim()
#@param col-name:notes
#@param expression:value.trim()
#@in table9
#@out table10
#@end core/text-transform9
#@begin core/text-transform10#@desc Text transform on cells in column location using expression value.trim()
#@param col-name:location
#@param expression:value.trim()
#@in table10
#@out table11
#@end core/text-transform10
#@begin core/text-transform11#@desc Text transform on cells in column status using expression value.trim()
#@param col-name:status
#@param expression:value.trim()
#@in table11
#@out table12
#@end core/text-transform11
#@begin core/text-transform12#@desc Text transform on cells in column status using expression value.replace(/\\s+/,' ')
#@param col-name:status
#@param expression:value.replace(/\\s+/,'_')
#@in table12
#@out table13
#@end core/text-transform12
#@begin core/text-transform13#@desc Text transform on cells in column location using expression value.replace(/\\s+/,' ')
#@param col-name:location
#@param expression:value.replace(/\\s+/,'_')
#@in table13
#@out table14
#@end core/text-transform13
#@begin core/text-transform14#@desc Text transform on cells in column notes using expression value.replace(/\\s+/,' ')
#@param col-name:notes
#@param expression:value.replace(/\\s+/,'_')
#@in table14
#@out table15
#@end core/text-transform14
#@begin core/text-transform15#@desc Text transform on cells in column notes using expression value.replace(/\\s+/,' ')
#@param col-name:notes
#@param expression:value.replace(/\\s+/,'_')
#@in table15
#@out table16
#@end core/text-transform15
#@begin core/text-transform16#@desc Text transform on cells in column occasion using expression value.replace(/\\s+/,' ')
#@param col-name:occasion
#@param expression:value.replace(/\\s+/,'_')
#@in table16
#@out table17
#@end core/text-transform16
#@begin core/text-transform17#@desc Text transform on cells in column physical_description using expression value.replace(/\\s+/,' ')
#@param col-name:physical_description
#@param expression:value.replace(/\\s+/,'_')
#@in table17
#@out table18
#@end core/text-transform17
#@begin core/text-transform18#@desc Text transform on cells in column place using expression value.replace(/\\s+/,' ')
#@param col-name:place
#@param expression:value.replace(/\\s+/,'_')
#@in table18
#@out table19
#@end core/text-transform18
#@begin core/text-transform19#@desc Text transform on cells in column venue using expression value.replace(/\\s+/,' ')
#@param col-name:venue
#@param expression:value.replace(/\\s+/,'_')
#@in table19
#@out table20
#@end core/text-transform19
#@begin core/text-transform20#@desc Text transform on cells in column event using expression value.replace(/\\s+/,' ')
#@param col-name:event
#@param expression:value.replace(/\\s+/,'_')
#@in table20
#@out table21
#@end core/text-transform20
#@begin core/text-transform21#@desc Text transform on cells in column sponsor using expression value.replace(/\\s+/,' ')
#@param col-name:sponsor
#@param expression:value.replace(/\\s+/,'_')
#@in table21
#@out table22
#@end core/text-transform21
#@begin core/text-transform22#@desc Text transform on cells in column id using expression value.toNumber()
#@param col-name:id
#@param expression:value.toNumber()
#@in table22
#@out table23
#@end core/text-transform22
#@begin core/text-transform23#@desc Text transform on cells in column call_number using expression value.trim()
#@param col-name:call_number
#@param expression:value.trim()
#@in table23
#@out table24
#@end core/text-transform23
#@begin core/text-transform24#@desc Text transform on cells in column call_number using expression value.replace(/\\s+/,' ')
#@param col-name:call_number
#@param expression:value.replace(/\\s+/,'_')
#@in table24
#@out table25
#@end core/text-transform24
#@begin core/text-transform25#@desc Text transform on cells in column page_count using expression value.toNumber()
#@param col-name:page_count
#@param expression:value.toNumber()
#@in table25
#@out table26
#@end core/text-transform25
#@begin core/text-transform26#@desc Text transform on cells in column dish_count using expression value.toNumber()
#@param col-name:dish_count
#@param expression:value.toNumber()
#@in table26
#@out table27
#@end core/text-transform26
#@begin core/text-transform27#@desc Text transform on cells in column sponsor using expression value.toTitlecase()
#@param col-name:sponsor
#@param expression:value.toTitlecase()
#@in table27
#@out table28
#@end core/text-transform27
#@begin core/text-transform28#@desc Text transform on cells in column event using expression value.toTitlecase()
#@param col-name:event
#@param expression:value.toTitlecase()
#@in table28
#@out table29
#@end core/text-transform28
#@begin core/text-transform29#@desc Text transform on cells in column venue using expression value.toTitlecase()
#@param col-name:venue
#@param expression:value.toTitlecase()
#@in table29
#@out table30
#@end core/text-transform29
#@begin core/text-transform30#@desc Text transform on cells in column place using expression value.toTitlecase()
#@param col-name:place
#@param expression:value.toTitlecase()
#@in table30
#@out table31
#@end core/text-transform30
#@begin core/text-transform31#@desc Text transform on cells in column physical_description using expression value.toTitlecase()
#@param col-name:physical_description
#@param expression:value.toTitlecase()
#@in table31
#@out table32
#@end core/text-transform31
#@begin core/text-transform32#@desc Text transform on cells in column occasion using expression value.toTitlecase()
#@param col-name:occasion
#@param expression:value.toTitlecase()
#@in table32
#@out table33
#@end core/text-transform32
#@begin core/text-transform33#@desc Text transform on cells in column notes using expression value.toTitlecase()
#@param col-name:notes
#@param expression:value.toTitlecase()
#@in table33
#@out table34
#@end core/text-transform33
#@begin core/text-transform34#@desc Text transform on cells in column location using expression value.toTitlecase()
#@param col-name:location
#@param expression:value.toTitlecase()
#@in table34
#@out table35
#@end core/text-transform34
#@begin core/text-transform35#@desc Text transform on cells in column status using expression value.toTitlecase()
#@param col-name:status
#@param expression:value.toTitlecase()
#@in table35
#@out table36
#@end core/text-transform35
#@begin core/text-transform36#@desc Text transform on cells in column currency using expression value.trim()
#@param col-name:currency
#@param expression:value.trim()
#@in table36
#@out table37
#@end core/text-transform36
#@begin core/text-transform37#@desc Text transform on cells in column currency using expression value.replace(/\\s+/,' ')
#@param col-name:currency
#@param expression:value.replace(/\\s+/,'_')
#@in table37
#@out table38
#@end core/text-transform37
#@begin core/text-transform38#@desc Text transform on cells in column currency using expression value.toTitlecase()
#@param col-name:currency
#@param expression:value.toTitlecase()
#@in table38
#@out table39
#@end core/text-transform38
#@begin core/text-transform39#@desc Text transform on cells in column call_number using expression value.trim()
#@param col-name:call_number
#@param expression:value.trim()
#@in table39
#@out table40
#@end core/text-transform39
#@begin core/text-transform40#@desc Text transform on cells in column call_number using expression value.replace(/\\s+/,' ')
#@param col-name:call_number
#@param expression:value.replace(/\\s+/,'_')
#@in table40
#@out table41
#@end core/text-transform40
#@begin core/text-transform41#@desc Text transform on cells in column date using expression value.toDate()
#@param col-name:date
#@param expression:value.toDate()
#@in table41
#@out table42
#@end core/text-transform41
#@begin core/text-transform42#@desc Text transform on cells in column date using expression grel:toString(toDate(value),\"yyyy-MM-dd\")
#@param col-name:date
#@param expression:grel:toString(toDate(value),"yyyy-MM-dd")
#@in table42
#@out table43
#@end core/text-transform42
#@begin core/text-transform43#@desc Text transform on cells in column event using expression grel:value.replace(/[\\[\\];?()\\*!]/,' ')
#@param col-name:event
#@param expression:grel:value.replace(/[\\[\\];?()\\*!]/,'_')
#@in table43
#@out table44
#@end core/text-transform43
#@begin core/text-transform44#@desc Text transform on cells in column event using expression grel:value.replace(/[\\[\\]\"\";?()\\*!]/,' ')
#@param col-name:event
#@param expression:grel:value.replace(/[\\[\\]"";?()\\*!]/,'_')
#@in table44
#@out table45
#@end core/text-transform44
#@begin core/text-transform45#@desc Text transform on cells in column event using expression grel:value.replace(/[\\[\\]\"\";?()\\*!']/,' ')
#@param col-name:event
#@param expression:grel:value.replace(/[\\[\\]"";?()\\*!']/,'_')
#@in table45
#@out table46
#@end core/text-transform45
#@begin core/text-transform46#@desc Text transform on cells in column event using expression value.toTitlecase()
#@param col-name:event
#@param expression:value.toTitlecase()
#@in table46
#@out table47
#@end core/text-transform46
#@begin core/text-transform47#@desc Text transform on cells in column event using expression value.trim()
#@param col-name:event
#@param expression:value.trim()
#@in table47
#@out table48
#@end core/text-transform47
#@begin core/text-transform48#@desc Text transform on cells in column event using expression value.replace(/\\s+/,' ')
#@param col-name:event
#@param expression:value.replace(/\\s+/,'_')
#@in table48
#@out table49
#@end core/text-transform48
#@begin core/mass-edit0#@desc Mass edit cells in column event
#@param col-name:event
#@in table49
#@out table50
#@end core/mass-edit0
#@begin core/mass-edit1#@desc Mass edit cells in column event
#@param col-name:event
#@in table50
#@out table51
#@end core/mass-edit1
#@begin core/mass-edit2#@desc Mass edit cells in column event
#@param col-name:event
#@in table51
#@out table52
#@end core/mass-edit2
#@begin core/mass-edit3#@desc Mass edit cells in column event
#@param col-name:event
#@in table52
#@out table53
#@end core/mass-edit3
#@begin core/mass-edit4#@desc Mass edit cells in column event
#@param col-name:event
#@in table53
#@out table54
#@end core/mass-edit4
#@begin core/mass-edit5#@desc Mass edit cells in column event
#@param col-name:event
#@in table54
#@out table55
#@end core/mass-edit5
#@begin core/mass-edit6#@desc Mass edit cells in column event
#@param col-name:event
#@in table55
#@out table56
#@end core/mass-edit6
#@begin core/text-transform49#@desc Text transform on cells in column event using expression value.trim()
#@param col-name:event
#@param expression:value.trim()
#@in table56
#@out table57
#@end core/text-transform49
#@begin core/text-transform50#@desc Text transform on cells in column event using expression value.replace(/\\s+/,' ')
#@param col-name:event
#@param expression:value.replace(/\\s+/,'_')
#@in table57
#@out table58
#@end core/text-transform50
#@begin core/mass-edit7#@desc Mass edit cells in column event
#@param col-name:event
#@in table58
#@out table59
#@end core/mass-edit7
#@begin core/mass-edit8#@desc Mass edit cells in column event
#@param col-name:event
#@in table59
#@out table60
#@end core/mass-edit8
#@begin core/mass-edit9#@desc Mass edit cells in column event
#@param col-name:event
#@in table60
#@out table61
#@end core/mass-edit9
#@begin core/mass-edit10#@desc Mass edit cells in column event
#@param col-name:event
#@in table61
#@out table62
#@end core/mass-edit10
#@begin core/mass-edit11#@desc Mass edit cells in column event
#@param col-name:event
#@in table62
#@out table63
#@end core/mass-edit11
#@begin core/mass-edit12#@desc Mass edit cells in column event
#@param col-name:event
#@in table63
#@out table64
#@end core/mass-edit12
#@begin core/mass-edit13#@desc Mass edit cells in column event
#@param col-name:event
#@in table64
#@out table65
#@end core/mass-edit13
#@begin core/mass-edit14#@desc Mass edit cells in column event
#@param col-name:event
#@in table65
#@out table66
#@end core/mass-edit14
#@begin core/mass-edit15#@desc Mass edit cells in column event
#@param col-name:event
#@in table66
#@out table67
#@end core/mass-edit15
#@begin core/mass-edit16#@desc Mass edit cells in column event
#@param col-name:event
#@in table67
#@out table68
#@end core/mass-edit16
#@begin core/mass-edit17#@desc Mass edit cells in column event
#@param col-name:event
#@in table68
#@out table69
#@end core/mass-edit17
#@begin core/mass-edit18#@desc Mass edit cells in column event
#@param col-name:event
#@in table69
#@out table70
#@end core/mass-edit18
#@begin core/mass-edit19#@desc Mass edit cells in column event
#@param col-name:event
#@in table70
#@out table71
#@end core/mass-edit19
#@begin core/mass-edit20#@desc Mass edit cells in column event
#@param col-name:event
#@in table71
#@out table72
#@end core/mass-edit20
#@begin core/mass-edit21#@desc Mass edit cells in column event
#@param col-name:event
#@in table72
#@out table73
#@end core/mass-edit21
#@begin core/mass-edit22#@desc Mass edit cells in column event
#@param col-name:event
#@in table73
#@out table74
#@end core/mass-edit22
#@begin core/mass-edit23#@desc Mass edit cells in column event
#@param col-name:event
#@in table74
#@out table75
#@end core/mass-edit23
#@begin core/mass-edit24#@desc Mass edit cells in column event
#@param col-name:event
#@in table75
#@out table76
#@end core/mass-edit24
#@begin core/mass-edit25#@desc Mass edit cells in column event
#@param col-name:event
#@in table76
#@out table77
#@end core/mass-edit25
#@begin core/mass-edit26#@desc Mass edit cells in column event
#@param col-name:event
#@in table77
#@out table78
#@end core/mass-edit26
#@begin core/mass-edit27#@desc Mass edit cells in column event
#@param col-name:event
#@in table78
#@out table79
#@end core/mass-edit27
#@begin core/mass-edit28#@desc Mass edit cells in column event
#@param col-name:event
#@in table79
#@out table80
#@end core/mass-edit28
#@begin core/mass-edit29#@desc Mass edit cells in column event
#@param col-name:event
#@in table80
#@out table81
#@end core/mass-edit29
#@begin core/mass-edit30#@desc Mass edit cells in column event
#@param col-name:event
#@in table81
#@out table82
#@end core/mass-edit30
#@begin core/mass-edit31#@desc Mass edit cells in column event
#@param col-name:event
#@in table82
#@out table83
#@end core/mass-edit31
#@begin core/mass-edit32#@desc Mass edit cells in column event
#@param col-name:event
#@in table83
#@out table84
#@end core/mass-edit32
#@begin core/mass-edit33#@desc Mass edit cells in column event
#@param col-name:event
#@in table84
#@out table85
#@end core/mass-edit33
#@begin core/mass-edit34#@desc Mass edit cells in column event
#@param col-name:event
#@in table85
#@out table86
#@end core/mass-edit34
#@begin core/mass-edit35#@desc Mass edit cells in column event
#@param col-name:event
#@in table86
#@out table87
#@end core/mass-edit35
#@begin core/mass-edit36#@desc Mass edit cells in column event
#@param col-name:event
#@in table87
#@out table88
#@end core/mass-edit36
#@begin core/text-transform51#@desc Text transform on cells in column event using expression value.trim()
#@param col-name:event
#@param expression:value.trim()
#@in table88
#@out table89
#@end core/text-transform51
#@begin core/text-transform52#@desc Text transform on cells in column event using expression value.replace(/\\s+/,' ')
#@param col-name:event
#@param expression:value.replace(/\\s+/,'_')
#@in table89
#@out table90
#@end core/text-transform52
#@begin core/mass-edit37#@desc Mass edit cells in column event
#@param col-name:event
#@in table90
#@out table91
#@end core/mass-edit37
#@begin core/mass-edit38#@desc Mass edit cells in column event
#@param col-name:event
#@in table91
#@out table92
#@end core/mass-edit38
#@begin core/mass-edit39#@desc Mass edit cells in column event
#@param col-name:event
#@in table92
#@out table93
#@end core/mass-edit39
#@begin core/mass-edit40#@desc Mass edit cells in column event
#@param col-name:event
#@in table93
#@out table94
#@end core/mass-edit40
#@begin core/column-addition0#@desc Create column event_grouped at index 4 based on column event using expression grel:value
#@param col-name:event
#@param newColumnName:"event_grouped"
#@in table94
#@out table95
#@end core/column-addition0
#@begin core/text-transform53#@desc Text transform on cells in column event_grouped using expression value.trim()
#@param col-name:event_grouped
#@param expression:value.trim()
#@in table95
#@out table96
#@end core/text-transform53
#@begin core/text-transform54#@desc Text transform on cells in column event_grouped using expression value.replace(/\\s+/,' ')
#@param col-name:event_grouped
#@param expression:value.replace(/\\s+/,'_')
#@in table96
#@out table97
#@end core/text-transform54
#@begin core/text-transform55#@desc Text transform on cells in column event_grouped using expression value.toTitlecase()
#@param col-name:event_grouped
#@param expression:value.toTitlecase()
#@in table97
#@out table98
#@end core/text-transform55
#@begin core/mass-edit41#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table98
#@out table99
#@end core/mass-edit41
#@begin core/mass-edit42#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table99
#@out table100
#@end core/mass-edit42
#@begin core/mass-edit43#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table100
#@out table101
#@end core/mass-edit43
#@begin core/mass-edit44#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table101
#@out table102
#@end core/mass-edit44
#@begin core/mass-edit45#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table102
#@out table103
#@end core/mass-edit45
#@begin core/mass-edit46#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table103
#@out table104
#@end core/mass-edit46
#@begin core/text-transform56#@desc Text transform on cells in column event_grouped using expression value.trim()
#@param col-name:event_grouped
#@param expression:value.trim()
#@in table104
#@out table105
#@end core/text-transform56
#@begin core/text-transform57#@desc Text transform on cells in column event_grouped using expression value.replace(/\\s+/,' ')
#@param col-name:event_grouped
#@param expression:value.replace(/\\s+/,'_')
#@in table105
#@out table106
#@end core/text-transform57
#@begin core/text-transform58#@desc Text transform on cells in column event_grouped using expression value.toTitlecase()
#@param col-name:event_grouped
#@param expression:value.toTitlecase()
#@in table106
#@out table107
#@end core/text-transform58
#@begin core/mass-edit47#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table107
#@out table108
#@end core/mass-edit47
#@begin core/mass-edit48#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table108
#@out table109
#@end core/mass-edit48
#@begin core/mass-edit49#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table109
#@out table110
#@end core/mass-edit49
#@begin core/mass-edit50#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table110
#@out table111
#@end core/mass-edit50
#@begin core/mass-edit51#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table111
#@out table112
#@end core/mass-edit51
#@begin core/mass-edit52#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table112
#@out table113
#@end core/mass-edit52
#@begin core/mass-edit53#@desc Mass edit cells in column event_grouped
#@param col-name:event_grouped
#@in table113
#@out table114
#@end core/mass-edit53
#@begin core/text-transform59#@desc Text transform on cells in column occasion using expression grel:value.replace(/[\\[\\]\"\";?()\\*!']/,' ')
#@param col-name:occasion
#@param expression:grel:value.replace(/[\\[\\]"";?()\\*!']/,'_')
#@in table114
#@out table115
#@end core/text-transform59
#@begin core/text-transform60#@desc Text transform on cells in column occasion using expression value.trim()
#@param col-name:occasion
#@param expression:value.trim()
#@in table115
#@out table116
#@end core/text-transform60
#@begin core/text-transform61#@desc Text transform on cells in column occasion using expression value.replace(/\\s+/,' ')
#@param col-name:occasion
#@param expression:value.replace(/\\s+/,'_')
#@in table116
#@out table117
#@end core/text-transform61
#@begin core/text-transform62#@desc Text transform on cells in column occasion using expression grel:value.replace(/[\\[\\]\"\";?()\\*!']/,' ')
#@param col-name:occasion
#@param expression:grel:value.replace(/[\\[\\]"";?()\\*!']/,'_')
#@in table117
#@out table118
#@end core/text-transform62
#@begin core/mass-edit54#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table118
#@out table119
#@end core/mass-edit54
#@begin core/mass-edit55#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table119
#@out table120
#@end core/mass-edit55
#@begin core/mass-edit56#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table120
#@out table121
#@end core/mass-edit56
#@begin core/mass-edit57#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table121
#@out table122
#@end core/mass-edit57
#@begin core/mass-edit58#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table122
#@out table123
#@end core/mass-edit58
#@begin core/mass-edit59#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table123
#@out table124
#@end core/mass-edit59
#@begin core/mass-edit60#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table124
#@out table125
#@end core/mass-edit60
#@begin core/mass-edit61#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table125
#@out table126
#@end core/mass-edit61
#@begin core/mass-edit62#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table126
#@out table127
#@end core/mass-edit62
#@begin core/mass-edit63#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table127
#@out table128
#@end core/mass-edit63
#@begin core/mass-edit64#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table128
#@out table129
#@end core/mass-edit64
#@begin core/mass-edit65#@desc Mass edit cells in column occasion
#@param col-name:occasion
#@in table129
#@out table130
#@end core/mass-edit65
#@begin core/text-transform63#@desc Text transform on cells in column occasion using expression value.trim()
#@param col-name:occasion
#@param expression:value.trim()
#@in table130
#@out table131
#@end core/text-transform63
#@begin core/text-transform64#@desc Text transform on cells in column occasion using expression value.replace(/\\s+/,' ')
#@param col-name:occasion
#@param expression:value.replace(/\\s+/,'_')
#@in table131
#@out table132
#@end core/text-transform64
#@end Linear_OR
