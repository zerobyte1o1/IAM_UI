###2021-12-23
已完成的测试：物料管理、物料类别

###2021-12-29
完成flow、group测试\
加入了环境配置，便于代码可以在不同的环境运行

###2021-12-31
显式等待的用法理解加深。

###2022-01-04
project页面代码\
svg元素特殊定位
```
//*[name()='svg']
```
###2022-01-07
项目管理测试用例梳理、代码编写

### 2022-01-08
>BUGS:\
fixed         - testcase/test_flow.py:16 TestFlow.test_update_flow_task\
fixed         - testcase/test_group_setting.py:20 TestGroupSetting.test_delete_member\
fixed         - testcase/test_group_setting.py:26 TestGroupSetting.test_delete_group\
fixed         - testcase/test_material_category.py:12 TestCreateMaterialCategory.test_create_material_category\
fixed         - testcase/test_material_category.py:17 TestCreateMaterialCategory.test_update_material_category\
fixed         - testcase/test_material_category.py:27 TestCreateMaterialCategory.test_delete_material_category_a\
fixed         - testcase/test_material_category.py:37 TestCreateMaterialCategory.test_delete_material_category_b\
暂没复现         - testcase/test_material_manage.py:31 TestMaterial.test_update_material\
暂没复现         - testcase/test_material_manage.py:46 TestMaterial.test_delete_material_a\
暂没复现         - testcase/test_project_manage.py:25 TestProject.test_start_with_product\
暂没复现         - testcase/test_project_manage.py:33 TestProject.test_check_product_options\
fixed         - testcase/test_project_manage.py:57 TestProject.test_check_task_act_buttons_under_inprocess\
暂没复现         - testcase/test_project_manage.py:68 TestProject.test_create_bom\
暂没复现         - testcase/test_project_manage.py:84 TestProject.test_update_bom\
暂没复现         - testcase/test_project_manage.py:98 TestProject.test_fill_bom_and_form_interaction\
fixed         - testcase/test_project_manage.py:111 TestProject.test_end_project_with_released_bom\

Group setting页面， 删除逻辑还要补充更多的用例：\
1.小组包含组员
2.小组已被项目使用。