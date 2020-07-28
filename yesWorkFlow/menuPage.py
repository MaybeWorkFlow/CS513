#@begin Parallel_OR #@desc Parallel OpenRefine Workflow
#@param expression:value.trim()
#@param expression:value.toNumber()
#@in full_width
#@in uuid
#@in menu_id_1
#@in menu_id
#@in full_height
#@in image_id
#@in page_number
#@in id_1
#@in id
#@out CleanData
#@begin core/text-transform0 #@desc Text transform on cells in column page_number using expression value.toNumber()
#@param expression:value.toNumber()
#@in page_number
#@out page_number_1
#@end core/text-transform0
#@begin core/text-transform1 #@desc Text transform on cells in column image_id using expression value.toNumber()
#@param expression:value.toNumber()
#@in image_id
#@out image_id_1
#@end core/text-transform1
#@begin core/text-transform2 #@desc Text transform on cells in column full_height using expression value.toNumber()
#@param expression:value.toNumber()
#@in full_height
#@out full_height_1
#@end core/text-transform2
#@begin core/text-transform3 #@desc Text transform on cells in column full_width using expression value.toNumber()
#@param expression:value.toNumber()
#@in full_width
#@out full_width_1
#@end core/text-transform3
#@begin core/text-transform4 #@desc Text transform on cells in column id using expression value.trim()
#@param expression:value.trim()
#@in id
#@out id_1
#@end core/text-transform4
#@begin core/text-transform5 #@desc Text transform on cells in column menu_id using expression value.trim()
#@param expression:value.trim()
#@in menu_id
#@out menu_id_1
#@end core/text-transform5
#@begin core/text-transform6 #@desc Text transform on cells in column uuid using expression value.trim()
#@param expression:value.trim()
#@in uuid
#@out uuid_1
#@end core/text-transform6
#@begin core/text-transform7 #@desc Text transform on cells in column id using expression value.toNumber()
#@param expression:value.toNumber()
#@in id_1
#@out id_2
#@end core/text-transform7
#@begin core/text-transform8 #@desc Text transform on cells in column menu_id using expression value.toNumber()
#@param expression:value.toNumber()
#@in menu_id_1
#@out menu_id_2
#@end core/text-transform8
#@begin CombineDataCleaningChanges
#@in page_number_1
#@in image_id_1
#@in full_height_1
#@in full_width_1
#@in id_2
#@in menu_id_2
#@in uuid_1
#@out CleanData
#@end CombineDataCleaningChanges
#@end Parallel_OR
