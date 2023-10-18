# 메뉴 출력 기능
def show_menu(menu_list):
    for i, menu in enumerate(main_list.values()):
        print(f"**  {i+1}.{menu}")