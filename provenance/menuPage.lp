% Menu Page Data Provenance
menuPage("core/text-transform0#", table1).
menuPage("col-name:page_number", "core/text-transform0#").
menuPage("expression:value.toNumber()", "core/text-transform0#").
menuPage(table0, "core/text-transform0#").
menuPage("core/text-transform1#", table2).
menuPage("col-name:image_id", "core/text-transform1#").
menuPage("expression:value.toNumber()", "core/text-transform1#").
menuPage(table1, "core/text-transform1#").
menuPage("core/text-transform2#", table3).
menuPage("col-name:full_height", "core/text-transform2#").
menuPage("expression:value.toNumber()", "core/text-transform2#").
menuPage(table2, "core/text-transform2#").
menuPage("core/text-transform3#", table4).
menuPage("col-name:full_width", "core/text-transform3#").
menuPage("expression:value.toNumber()", "core/text-transform3#").
menuPage(table3, "core/text-transform3#").
menuPage("core/text-transform4#", table5).
menuPage("col-name:id", "core/text-transform4#").
menuPage("expression:value.trim()", "core/text-transform4#").
menuPage(table4, "core/text-transform4#").
menuPage("core/text-transform5#", table6).
menuPage("col-name:menu_id", "core/text-transform5#").
menuPage("expression:value.trim()", "core/text-transform5#").
menuPage(table5, "core/text-transform5#").
menuPage("core/text-transform6#", table7).
menuPage("col-name:uuid", "core/text-transform6#").
menuPage("expression:value.trim()", "core/text-transform6#").
menuPage(table6, "core/text-transform6#").
menuPage("core/text-transform7#", table8).
menuPage("col-name:id", "core/text-transform7#").
menuPage("expression:value.toNumber()", "core/text-transform7#").
menuPage(table7, "core/text-transform7#").
menuPage("core/text-transform8#", table9).
menuPage("col-name:menu_id", "core/text-transform8#").
menuPage("expression:value.toNumber()", "core/text-transform8#").
menuPage(table8, "core/text-transform8#").

menuPage_provenance(X,Y) :- menuPage(X,Y).
menuPage_provenance(X,Y) :- menuPage(X,Z), menuPage(Z,Y).

ans(X) :- menuPage_provenance(X, table9).

#show ans/1.