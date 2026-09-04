import streamlit as st

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="ShopEasy",
    page_icon="🛒",
    layout="wide"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(135deg, #f5f7ff, #eef2ff);
}

/* Title */
.main-title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #1f3c88;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #555;
    margin-bottom: 30px;
}

/* Product cards */
.product-card {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
    margin-bottom: 20px;
    text-align: center;
}

/* Product image */
.product-image img {
    border-radius: 12px;
}

/* Price */
.price {
    font-size: 22px;
    font-weight: bold;
    color: #16a34a;
}

/* Home box */
.hero-box {
    background: linear-gradient(135deg, #2563eb, #7c3aed);
    color: white;
    padding: 40px;
    border-radius: 20px;
    text-align: center;
    margin-bottom: 30px;
}

/* Feature boxes */
.feature-box {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
}

/* Cart item */
.cart-box {
    background-color: white;
    padding: 15px;
    border-radius: 15px;
    margin-bottom: 15px;
    box-shadow: 0px 3px 10px rgba(0,0,0,0.1);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #1e293b;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white;
}

</style>
""", unsafe_allow_html=True)


# ==========================================
# PRODUCTS
# ==========================================

products = [
    {
        "id": 1,
        "name": "Laptop",
        "price": 50000,
        "icon": "💻",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1496181133206-80ce9b88a853?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 2,
        "name": "Mobile",
        "price": 20000,
        "icon": "📱",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1511707171634-5f897ff02aa0?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 3,
        "name": "Headphones",
        "price": 2000,
        "icon": "🎧",
        "category": "Accessories",
        "image": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 4,
        "name": "Smart Watch",
        "price": 5000,
        "icon": "⌚",
        "category": "Accessories",
        "image": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 5,
        "name": "Camera",
        "price": 30000,
        "icon": "📷",
        "category": "Electronics",
        "image": "https://images.unsplash.com/photo-1516035069371-29a1b244cc32?auto=format&fit=crop&w=600&q=80"
    },
    {
        "id": 6,
        "name": "Keyboard",
        "price": 1500,
        "icon": "⌨️",
        "category": "Accessories",
        "image": "https://images.unsplash.com/photo-1587829741301-dc798b83add3?auto=format&fit=crop&w=600&q=80"
    }
]


# ==========================================
# CART
# ==========================================

if "cart" not in st.session_state:
    st.session_state.cart = []


# ==========================================
# HEADER
# ==========================================

st.markdown(
    '<div class="main-title">🛒 ShopEasy</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Your Favourite Online Shopping Store</div>',
    unsafe_allow_html=True
)


# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown(
    "# 🛒 ShopEasy"
)

st.sidebar.write(
    "🛍️ Happy Shopping!"
)

st.sidebar.divider()

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "🛍️ Products",
        "🛒 Cart"
    ]
)

st.sidebar.divider()

st.sidebar.markdown(
    f"### 🛒 Cart Items: {len(st.session_state.cart)}"
)


# ==========================================
# HOME PAGE
# ==========================================

if page == "🏠 Home":

    st.markdown("""
    <div class="hero-box">
        <h1>Welcome to ShopEasy 🛍️</h1>
        <h3>Your One-Stop Online Shopping Destination</h3>
        <p>Buy amazing products at the best prices!</p>
    </div>
    """, unsafe_allow_html=True)

    st.image(
        "https://images.unsplash.com/photo-1556742049-0cfed4f6a45d?auto=format&fit=crop&w=1400&q=80",
        use_container_width=True
    )

    st.markdown("## ⭐ Why Choose ShopEasy?")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="feature-box">
        <h2>🚚</h2>
        <h4>Fast Delivery</h4>
        <p>Quick and safe delivery.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-box">
        <h2>💳</h2>
        <h4>Secure Payment</h4>
        <p>100% safe payments.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-box">
        <h2>⭐</h2>
        <h4>Best Quality</h4>
        <p>Premium quality products.</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature-box">
        <h2>🔄</h2>
        <h4>Easy Returns</h4>
        <p>Simple return process.</p>
        </div>
        """, unsafe_allow_html=True)


# ==========================================
# PRODUCTS PAGE
# ==========================================

elif page == "🛍️ Products":

    st.header("🛍️ Explore Our Products")

    col1, col2 = st.columns(2)

    with col1:
        search = st.text_input(
            "🔍 Search Product",
            placeholder="Search here..."
        )

    with col2:
        category = st.selectbox(
            "🏷️ Category",
            [
                "All",
                "Electronics",
                "Accessories"
            ]
        )


    # FILTER PRODUCTS

    filtered_products = []

    for product in products:

        category_match = (
            category == "All"
            or product["category"] == category
        )

        search_match = (
            search.lower()
            in product["name"].lower()
        )

        if category_match and search_match:

            filtered_products.append(
                product
            )


    # PRODUCT GRID

    cols = st.columns(3)

    for index, product in enumerate(
        filtered_products
    ):

        with cols[index % 3]:

            st.markdown(
                '<div class="product-card">',
                unsafe_allow_html=True
            )

            st.image(
                product["image"],
                use_container_width=True
            )

            st.subheader(
                product["icon"]
                + " "
                + product["name"]
            )

            st.caption(
                "Category: "
                + product["category"]
            )

            st.markdown(
                f'<div class="price">₹ {product["price"]:,}</div>',
                unsafe_allow_html=True
            )

            st.write("")

            if st.button(
                "🛒 Add to Cart",
                key=f"add_{product['id']}",
                use_container_width=True
            ):

                st.session_state.cart.append(
                    product
                )

                st.success(
                    "Added to cart! 🎉"
                )

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )


# ==========================================
# CART PAGE
# ==========================================

elif page == "🛒 Cart":

    st.header("🛒 Your Shopping Cart")

    if len(st.session_state.cart) == 0:

        st.markdown("""
        <div class="feature-box">
            <h2>🛒</h2>
            <h3>Your cart is empty!</h3>
            <p>Go to Products and add your favourite items.</p>
        </div>
        """, unsafe_allow_html=True)


    else:

        total = 0

        for index, item in enumerate(
            st.session_state.cart
        ):

            st.markdown(
                '<div class="cart-box">',
                unsafe_allow_html=True
            )

            col1, col2, col3, col4 = st.columns(
                [2, 3, 2, 1]
            )

            with col1:

                st.image(
                    item["image"],
                    width=150
                )

            with col2:

                st.subheader(
                    item["icon"]
                    + " "
                    + item["name"]
                )

                st.write(
                    item["category"]
                )

            with col3:

                st.write("### Price")

                st.write(
                    f"₹ {item['price']:,}"
                )

            with col4:

                if st.button(
                    "🗑️ Remove",
                    key=f"remove_{index}"
                ):

                    st.session_state.cart.pop(
                        index
                    )

                    st.rerun()

            st.markdown(
                '</div>',
                unsafe_allow_html=True
            )

            total += item["price"]


        # ORDER SUMMARY

        st.divider()

        st.markdown(
            f"""
            <div class="hero-box">
                <h2>💰 Total Amount</h2>
                <h1>₹ {total:,}</h1>
            </div>
            """,
            unsafe_allow_html=True
        )

        col1, col2 = st.columns(2)

        with col1:

            if st.button(
                "🗑️ Clear Cart",
                use_container_width=True
            ):

                st.session_state.cart = []

                st.rerun()

        with col2:

            if st.button(
                "🎉 Place Order",
                use_container_width=True
            ):

                st.success(
                    "🎉 Your order has been placed successfully!"
                )

                st.balloons()

                st.session_state.cart = []