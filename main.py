from flet import *
import asyncio

class ProductPage(View) :
    def __init__(self, page, src, title, sub_title, price, rating : str):
        super().__init__(
            bgcolor = "#0c0f14"
        )
        self.page = page
        self.img_src = src
        self.img_src = src
        self.title = title
        self.sub_title = sub_title
        self.price = price
        self.rating = rating
        self.color_food = "#b9894b"
        self.bg_color = "#0c0f14"
        self.container_color = "#141821"
        self.build_view()
        
        
    def build_view(self) :
        self.controls.append(
            Container(
                alignment = alignment.center,
                bgcolor = self.bg_color,
                margin = 10,
                expand = True,
                content = 
                
                Column(
                    alignment = MainAxisAlignment.CENTER,
                    horizontal_alignment = CrossAxisAlignment.CENTER,
                    expand = True,
                    controls = [
                        Row(
                                   alignment = MainAxisAlignment.SPACE_BETWEEN,
                                   controls = [
                                       Container(
                                           on_click = self.close_productpage,
                                           width = 30,
                                           height = 30,
                                           border_radius = 10,
                                           bgcolor = "black",
                                           content = Icon(
                                               icons.KEYBOARD_ARROW_LEFT,
                                               color = self.color_food
                                           )
                                       ),
                                                                              Container(
                                           on_click = self.close_productpage,
                                           width = 30,
                                           height = 30,
                                           border_radius = 10,
                                           bgcolor = "black",
                                           content = Icon(
                                               icons.FAVORITE,
                                               color = self.color_food
                                           )
                                       ),
                                   ], 
                                ),
                        Stack(
                            expand = 8,
                            controls = [
                                
                                Container(
                                    alignment = alignment.center,
                                    border_radius = 20,
                                    content = 
                                        Image(
                                        src = self.img_src,
                                        fit = ImageFit.COVER,
                                        width = 350,
                                        height = 400,
                                    ),
                                    
                                ),
                               
                                Container(
                                    bgcolor = colors.with_opacity(0.6, "black"),
                                    border_radius = border_radius.only(bottom_left=20, bottom_right=20),
                                    expand = True,
                                    padding = 20,
                                    alignment = alignment.center_left,
                                    margin = margin.only(top = 200),
                                    shadow = BoxShadow(
                                        spread_radius = 15,
                                        blur_radius = 20,
                                        color = colors.with_opacity(0.3, "black"),
                                    ),
                                    content = Column(
                                        spacing = 2,
                                        controls = [
                                            Text(self.title, size = 30, weight = "bold"),
                                            Text(self.sub_title, size = 20, weight = "bold"),
                                            Row(
                                                controls = [
                                                    Text("₦", color = self.color_food),
                                                    Text(self.price, weight = "bold")
                                                ],
                                                spacing = 1,
                                            )
                                        ]
                                    )
                                )
                            
                            ]
                        ),
                        Container(
                            height = 30,
                            alignment = alignment.center_left,
                            content = Text("Size"),
                        ),
                        
                        Row(
                            expand = 1,
                            alignment = MainAxisAlignment.SPACE_AROUND,
                            controls = [
                                ElevatedButton(
                                    "S",
                                    color = "white",
                                     bgcolor = self.container_color,
                                     width = 80,
                                     style = ButtonStyle(overlay_color = {"hovered" : self.color_food},
                                                         elevation = 20, shape = RoundedRectangleBorder(radius = 10),
                                                         side = BorderSide(1, self.color_food)
                                                         )
                                ),
                                ElevatedButton(
                                    "M",
                                    color = "white",
                                     bgcolor = self.container_color,
                                     width = 80,
                                     style = ButtonStyle(overlay_color = {"hovered" : self.color_food},
                                                         elevation = 20, shape = RoundedRectangleBorder(radius = 10),
                                                         side = BorderSide(1, self.color_food)
                                                         )
                                ),
                                ElevatedButton(
                                    "L",
                                    color = "white",
                                     bgcolor = self.container_color,
                                     width = 80,
                                     style = ButtonStyle(overlay_color = {"hovered" : self.color_food},
                                                         elevation = 20, shape = RoundedRectangleBorder(radius = 10),
                                                         side = BorderSide(1, self.color_food)
                                                         )
                                )
                            ]
                        ),

                        Container(
                            height = 30,
                            alignment = alignment.center_left,
                            content = Text("Price"),
                        ),
                        Row(
                            expand = 1,
                            alignment = MainAxisAlignment.SPACE_BETWEEN,
                            controls = [
                                Text(
                                    spans=[
                                        TextSpan("₦", style = TextStyle(color = self.color_food, size = 20, weight = "bold"), ),
                                        TextSpan(f"{self.price}", style = TextStyle(color = "white", size = 20, weight = "bold"), )
                                    ]
                                ),
                                ElevatedButton(
                                    "Buy",
                                    color = "white",
                                     bgcolor = self.container_color,
                                     width = 80,
                                     style = ButtonStyle(overlay_color = {"hovered" : self.color_food},
                                                         elevation = 20, shape = RoundedRectangleBorder(radius = 10),
                                                         side = BorderSide(1, self.color_food)
                                                         )
                                ),
                            
                            ]
                        ),
                    ]
                ),
                
            )
        )
        
        
        
    def close_productpage(self,e) :
        self.page.views.pop()
        self.page.update()
        
    def add_favorites(self,e) :
        pass
    


class ProductCard(Container) :
    def __init__(self, page, src, title, sub_title, price, rating : str):
        super().__init__(
            alignment = alignment.center,
            width = 150,
            height = 150,
            border_radius = 10,
            bgcolor = "#141821",
            margin = margin.only(top = 10),
            padding = 10
        )
        
        self.page = page
        self.page_extra = page
        self.img_src = src
        self.img_src = src
        self.title = title
        self.sub_title = sub_title
        self.price = price
        self.rating = rating
        self.color_food = "#b9894b"
        self.bg_color = "#0c0f14"
        self.container_color = "#141821"
        
        page = self.page
        
        self.content = Column(
            expand = True,
            scroll = True,
            spacing = 0,
            controls = [
                
                Stack(
                    controls = [
                        Container(
                            border_radius = 10,
                            on_click = self.show_container,
                            content = Image(src = self.img_src, width = 150, fit = ImageFit.COVER, height = 100,)
                            
                        ),
                        Container(
                            width = 60,
                            alignment = alignment.center,
                            border_radius = border_radius.only(top_left = 10, bottom_right = 10),
                            bgcolor = colors.with_opacity(0.6, "black"),
                            content = Row(
                                spacing = 5,
                                controls = 
                                [Icon(icons.STAR_SHARP, color = self.color_food),
                                 Text(f"{self.rating}", weight = "bold", )
                                 
                                 ]
                            )
                        )
                    ]
                ),
            Text(value = self.title, weight = "bold"),
            Text(value = self.sub_title, color = "#5a5a5a"),
            Row(
                alignment = MainAxisAlignment.SPACE_BETWEEN,
                controls = [
                    Text(
                        spans=[
                            TextSpan("₦", style = TextStyle(color = self.color_food, size = 15, weight = "bold"), ),
                            TextSpan(f"{self.price}", style = TextStyle(color = "white", size = 15, weight = "bold"), )
                        ]
                    ),
                    Container(
                        content = Icon(icons.ADD, color = "white",),
                        bgcolor = self.color_food,
                        width = 30,
                        height = 30,
                        border_radius = 10,
                        on_click = self.add_favorites
                    )
                
                ]
            )
            ]
        )
        
    
    def show_container(self,e) :
        product_view = ProductPage(self.page, self.img_src, self.title, self.sub_title, self.price, self.rating)
        # if not self.page:
        #     print("Page is missing. Trying to fetch again...")
            
        # if self.page:
        #     self.page.views.append(product_view)
        #     self.page.update()
        
        
        if self.page :
            print ('the page exists')
            print(f'this is the extra page {self.page_extra.views}')
        else : 
            self.page = self.page_extra
            print(f"this is the page after setting the page to page_extra{self.page.views}")
        
        self.page.views.append(product_view)
        self.page.update()
    
    def add_favorites(self,e) :
        pass
        
    
class AppFood(Container) :
    def __init__(self, page : Page):
        super().__init__()
        
        self.page = page
        self.page_extra = page
        self.color_food = "#b9894b"
        self.bg_color = "#0c0f14"
        self.container_color = "#141821"
        self.nav_color = "#18191b"
        self.page.spacing = 5
        self.page.padding = 5
        self.page.bg_color = self.bg_color
        self.page.theme = Theme(scrollbar_theme=ScrollbarTheme(thumb_color=self.color_food),)
        # self.page.window_width = 390  # Set window width
        # self.page.window_height = 700  # Set window height
        
        # Responsive values
        self.runs_count = 3
        self.child_aspect_ratio = 1




        
        
        self.products = [
            ProductCard(self.page, "/egusipyam.jpg", "Egusi Soup and Pounded Yam", "A serving of our expertly prepared egusi soup and pouded yam",
                        "2500", "4.7"),
            ProductCard(self.page, "/fried rice.jpg", "Fried Rice", "A plate of our expertly prepared fried rice",
                        "2500", "4.3"),
            ProductCard(self.page, "/riceandstew.jpg", "White Rice and Stew", "A plate of our expertly prepared jollof rice",
                        "2500", "4.5"),
            ProductCard(self.page, "/fufu.jpg", "Fufu and Ogbono Soup", "A serving of our expertly prepared ogbono soup and fufu",
                        "2500", "4.3"),
            ProductCard(self.page, "/jellofrice.jpg", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                        "2500", "4.3"),
            ProductCard(self.page, "/jollof.png", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                        "2500", "4.3"),
            ProductCard(self.page, "/jollof.png", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                        "2500", "4.3"),
            ProductCard(self.page, "/jollof.png", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                        "2500", "4.3")
        ]
        
        self.runs_count = 3
        self.child_aspect_ratio = 1
        
       # Create the initial GridView
        self.grid_view = self.create_grid_view()
        
        self.container1 = Container(
            padding = 10,
            offset = transform.Offset(0.0,0.0),
            content = Column(
                expand = True,
                controls = [
                    Row(
                        alignment = MainAxisAlignment.SPACE_BETWEEN,
                        controls = [
                            IconButton(icon = icons.MENU, icon_color = "white"),
                            Container(
                                border_radius = 10,
                                content=Image(
                                    src = "/jelo.png",
                                    height = 30,
                                )
                            )
                            
                        ]
                    ),
                Text("Main Encounter \n Cafe le mois", size = 25,  weight = "bold"),
                TextField(prefix_icon = icons.SEARCH, hint_text = "Something", border_radius = 10,
                           bgcolor = self.container_color, border_color = "transparent",
                           on_change = self.filter_products 
                             ),
                Container(
                    expand = True,
                    content = Tabs(
                        selected_index = 0,
                        expand = True,
                        indicator_color = "transparent",
                        label_color = self.color_food,
                        tabs = [
                            Tab(
                                text = "Main Course",
                                 content = self.grid_view
                                
                            ),
                            Tab(
                                text = "Appetizers",
                                content = GridView(
                                    runs_count = self.runs_count,#self.runs_count,
                                    child_aspect_ratio = self.child_aspect_ratio,#self.child_aspect_ratio,
                                    on_scroll_interval = 1,
                                    controls = [
                                                ProductCard(self.page, "egusipyam.jpg", "Egusi Soup and Pounded Yam", "A serving of our expertly prepared egusi soup and pouded yam",
                                                            "2500", "4.7"),
                                                ProductCard(self.page, "/jollof.png", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                                                            "2500", "4.3"),
                                                ProductCard(self.page, "/jollof.png", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                                                            "2500", "4.3"),
                                                ProductCard(self.page, "/jollof.png", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                                                            "2500", "4.3"),
                                                ProductCard(self.page, "/jollof.png", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                                                            "2500", "4.3"),
                                                ProductCard(self.page, "/jollof.png", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                                                            "2500", "4.3"),
                                                ProductCard(self.page, "/jollof.png", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                                                            "2500", "4.3"),
                                                ProductCard(self.page, "/jollof.png", "Jollof Rice", "A plate of our expertly prepared jollof rice",
                                                            "2500", "4.3")
                                    ]
                                ) 
                            ),
                            Tab(
                                text = "Desserts",
                                content = self.grid_view
                            ),
                            Tab(
                                text = "Cusines",
                                content = GridView(
                                    runs_count = 2,
                                    child_aspect_ratio = 0.0,
                                    controls = [
                                        
                                    ]
                                ) 
                            ),
                            Tab(
                                text = "Chef's Special",
                                content = GridView(
                                    runs_count = 2,
                                    child_aspect_ratio = 0.0,
                                    controls = [
                                        
                                    ]
                                ) 
                            )
                        ]
                    )
                )    
                ]

            )
        )
        
        self.container_2 = Container(
            expand = True,
            offset = transform.Offset(2,0),
            content = Column(
                expand = True,
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment = CrossAxisAlignment.CENTER,
                controls = [
                    Text("Store", size = 20, ),
                    Container(
                        alignment = alignment.center,
                        content = Image(src = "assets/jelo.png", fit = ImageFit.CONTAIN, width = 100,)
                    )
                ]
            )
        )
        
        
        self.container_3 = Container(
            expand = True,
            offset = transform.Offset(2,0),
            content = Column(
                expand = True,
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment = CrossAxisAlignment.CENTER,
                controls = [
                    Text("Favourites", size = 20, ),
                    Container(
                        alignment = alignment.center,
                        content = Image(src = "assets/jelo.png", fit = ImageFit.CONTAIN, width = 100,)
                    )
                ]
            )
        )
        
        
        self.container_4 = Container(
            expand = True,
            offset = transform.Offset(2,0),
            content = Column(
                expand = True,
                alignment = MainAxisAlignment.CENTER,
                horizontal_alignment = CrossAxisAlignment.CENTER,
                controls = [
                    Text("Notifications", size = 20, ),
                    Container(
                        alignment = alignment.center,
                        content = Image(src = "assets/jelo.png", fit = ImageFit.CONTAIN, width = 100,)
                    )
                ]
            )
        )
        
        

        
        self.selected = Container(
            shape = BoxShape.CIRCLE,
            offset = transform.Offset(-0.38,0),
            bgcolor = self.nav_color,
            alignment = alignment.center,
            margin = margin.only(top = 10),
            height = 40,
            content = Icon(icons.HOME_FILLED, color = self.color_food)
        )
        
        self.nav = Container(
            bgcolor = self.nav_color,
            alignment = alignment.center,
            border_radius = 10,
            padding = 0,
            height = 50,
            margin = margin.only(top = 5),
            content = Row(
                alignment = MainAxisAlignment.SPACE_AROUND,
                controls = [
                    IconButton(icon = icons.HOME_FILLED, data = "1", icon_color = "white", on_click = self.change_position),
                    IconButton(icon = icons.SHOPPING_BAG_ROUNDED, data = "2", icon_color = "white", on_click = self.change_position),
                    IconButton(icon = icons.FAVORITE, data = "3", icon_color = "white", on_click = self.change_position),
                    IconButton(icon = icons.NOTIFICATIONS, data = "4", icon_color = "white", on_click = self.change_position),
                    # IconButton(icon = icons.HOME_FILLED, data = "1", icon_color = "white", on_click = self.change_position)
                ]
            )
        )
        
        self.page.add(
            Column(
                expand = True,
                controls=[
                    Stack(
                        expand = True,
                        controls = [
                           self.container1,
                           self.container_2,
                           self.container_3,
                           self.container_4
                        ]
                    ),
                    Stack(
                        height = 60,
                        controls = [
                            self.nav,
                            self.selected

                        ]
                    )
                ]
            )
        )
        # self.page.on_resized = self.on_resize
        self.page.on_resized = self.on_resize
        
    def create_grid_view(self):
        """
        Helper function to create a GridView with current properties.
        """
        return GridView(
            runs_count=self.runs_count,
            child_aspect_ratio=self.child_aspect_ratio,
            controls=self.products,
        )
    
    
    async def on_resize(self, e):
        """
        Update runs_count and child_aspect_ratio based on page width, and refresh the GridView.
        """
        if self.page.width < 600:  # Mobile view
            self.runs_count = 2
            self.child_aspect_ratio = 0.75
        elif self.page.width > 600 and self.page.width < 1000:
            self.runs_count = 3
            self.child_aspect_ratio = 1.2
        elif self.page.width > 1000 :  # Desktop view
            self.runs_count = 4
            self.child_aspect_ratio = 1.5

        # Log updated properties for debugging
        print(f"Updated GridView: runs_count={self.runs_count}, child_aspect_ratio={self.child_aspect_ratio}")
        print(f"Page width: {self.page.width}")
    
        
        # Recreate the GridView and update the Tabs content
        self.grid_view = self.create_grid_view()
        # Update the Main Course tab with the new GridView
        self.container1.content.controls[3].content.tabs[0].content = self.grid_view
        
        #     self.page.update()
        # await asyncio.sleep(0.1)  # Small delay
        # if self.page:
        #     self.page.update()
        # else:
        #     print("Page is None after delay.")
        # if self.page_extra.views == self.page.views:
            
        #     print(f'this is the extra page after resizing {self.page_extra.views}')
        # Force an update of the page to reflect changes
        self.page.update()    

    
    def filter_products(self,e) :
        search_text = e.control.value.lower()
        filtered_products = [
            product for product in self.products if search_text in product.title.lower()
            
        ]
        self.grid_view.controls = filtered_products
        self.grid_view.update()
        
    
    def change_position(self,e) :
        if e.control.data == "1" :
            self.selected.offset = transform.Offset(-0.38, 0)
            self.selected.content = Icon(icons.HOME_FILLED, color = self.color_food)
            self.container1.offset = transform.Offset(0.0, 0.0)
            self.container_2.offset = transform.Offset(-2, 0.0)
            self.container_3.offset = transform.Offset(-2, 0.0)
            self.container_4.offset = transform.Offset(-2, 0.0)
            
        if e.control.data == "2" :
            self.selected.offset = transform.Offset(-0.12, 0)
            self.selected.content = Icon(icons.SHOPPING_BAG_ROUNDED, color = self.color_food)
            self.container1.offset = transform.Offset(-2, 0.0)
            self.container_2.offset = transform.Offset(0.0, 0.0)
            self.container_3.offset = transform.Offset(-2, 0.0)
            self.container_4.offset = transform.Offset(-2, 0.0)
            
        if e.control.data == "3" :
            self.selected.offset = transform.Offset(0.12, 0)
            self.selected.content = Icon(icons.FAVORITE, color = self.color_food)
            self.container1.offset = transform.Offset(-2, 0.0)
            self.container_2.offset = transform.Offset(-2, 0.0)
            self.container_3.offset = transform.Offset(0.0, 0.0)
            self.container_4.offset = transform.Offset(-2, 0.0)
            
        if e.control.data == "4" :
            self.selected.offset = transform.Offset(0.38, 0)
            self.selected.content = Icon(icons.NOTIFICATIONS, color = self.color_food)
            self.container1.offset = transform.Offset(-2, 0.0)
            self.container_2.offset = transform.Offset(-2, 0.0)
            self.container_3.offset = transform.Offset(-2, 0.0)
            self.container_4.offset = transform.Offset(0.0, 0.0)
        
        self.page.update()
        
    def update_page(self) :
        self.page.update()
       

app(target =  lambda page : AppFood(page), view="web_browser",assets_dir="assets")
