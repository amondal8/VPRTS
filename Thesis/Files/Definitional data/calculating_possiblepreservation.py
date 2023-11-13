import utilities_dataset as ut_ds
import utilities as ut
import data as dt

ds_id = dt.ds_id
W = dt.W    # The capacity of the knapsack
def creating_valandwt(ds_id, rel_id = 1):
    us_tc_dict = dict()
    tccount_list = []
    query1 = f"Select us_id, us_businessvalue from userstory_datasettable where ds_id='{ds_id}' and release_id = {rel_id} order by us_id"
    print(query1)
    us_res = ut_ds.running_searchqury(query1)
    # print(us_res)
    us_list = ut.createlist_fromdbresult(us_res,0)
    usbv_list = ut.createlist_fromdbresult(us_res,1)
    print(us_list)
    print(usbv_list)
    query2 = f"Select us_id, Count(tc_id) from us_tc_map where ds_id={ds_id} and us_id in({str(us_list).replace('[','').replace(']','')}) group by us_id"
    us_res1 = ut_ds.running_searchqury(query2)
    for i in us_res1:
        us_tc_dict[i[0]] = i[1]
    print(us_tc_dict)

    for i in us_list:
        try:
            tccount_list.append(us_tc_dict[i])
        except:
            tccount_list.append(0)
            continue
    print(tccount_list)

    return usbv_list, tccount_list

for indi, i in enumerate(ds_id):
    usbv_list, tccount_list = creating_valandwt(i)
    preserved_val = ut_ds.knapsack_01(usbv_list, tccount_list, W[indi])
    ut_ds.readandwrite_toexcel(i, "B", preserved_val)
