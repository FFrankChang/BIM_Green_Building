import ifcopenshell

def read_ifc_buildings(ifc_file_path):
    # 加载 IFC 文件
    ifc_file = ifcopenshell.open(ifc_file_path)
    
    # 获取文件中所有的 IfcBuilding 对象
    buildings = ifc_file.by_type('IfcBuilding')
    
    # 遍历所有建筑物对象并打印相关信息
    for building in buildings:
        print(f"Building Name: {building.Name}")
        print(f"Building ID: {building.GlobalId}")
        print(f"Description: {building.Description if building.Description else 'No Description'}")
        print("-" * 40)

# 指定 IFC 文件的路径
ifc_file_path = 'path_to_your_ifc_file.ifc'

# 调用函数
read_ifc_buildings(ifc_file_path)
