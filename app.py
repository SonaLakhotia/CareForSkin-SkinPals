import streamlit as st

# Main Streamlit app
def main():
    st.title("Personalized Skin Care Routine")
    st.markdown("Upload a selfie to get personalized skin care recommendations.")

    # File uploader for image
    uploaded_file = st.file_uploader("Upload a selfie", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display the uploaded image
        st.image(uploaded_file, caption='Uploaded Image.', use_column_width=True)

        # Form inputs for skin type and concerns
        skin_type = st.radio("Select your skin type:", ("Normal", "Dry", "Oily", "Combination"))
        skin_concerns = st.multiselect("Select your skin concerns:", ("Acne", "Aging", "Sensitive", "Dryness"))

        if st.button("Get My Skin Care Routine"):
            # Rule-based recommendations
            recommended_products = get_recommendations(skin_concerns)
            routine_steps = get_routine(skin_type)

            # Display recommended routine and products
            st.subheader("Your Recommended Skin Care Routine:")
            st.write(", ".join(routine_steps))

            st.subheader("Recommended Products:")
            for product in recommended_products:
                st.write(product)

def get_recommendations(skin_concerns):
    # Rule-based function to return recommended products based on skin type and concerns
    recommended_products = []

    if "Acne" in skin_concerns:
        recommended_products.append("Salicylic Acid Cleanser")
        recommended_products.append("Oil-free Moisturizer")
        recommended_products.append("Spot Treatment Gel")

    if "Aging" in skin_concerns:
        recommended_products.append("Retinol Serum")
        recommended_products.append("Hydrating Eye Cream")
        recommended_products.append("Broad Spectrum Sunscreen")

    if "Sensitive" in skin_concerns:
        recommended_products.append("Gentle Cleansing Lotion")
        recommended_products.append("Hypoallergenic Moisturizer")

    if "Dryness" in skin_concerns:
        recommended_products.append("Hydrating Cleansing Balm")
        recommended_products.append("Rich Moisturizing Cream")
        recommended_products.append("Facial Oil")

    return recommended_products

def get_routine(skin_type):
    # Rule-based function to return skin care routine steps based on skin type
    if skin_type == "Normal":
        return ["Cleanser", "Toner", "Moisturizer", "Serum", "Sunscreen"]

    elif skin_type == "Dry":
        return ["Hydrating Cleanser", "Hydrating Toner", "Rich Moisturizer", "Facial Oil", "Sunscreen"]

    elif skin_type == "Oily":
        return ["Oil-control Cleanser", "Mattifying Toner", "Lightweight Moisturizer", "Serum", "Sunscreen"]

    elif skin_type == "Combination":
        return ["Balancing Cleanser", "Hydrating Toner", "Lightweight Moisturizer", "Targeted Serum", "Sunscreen"]




if __name__ == "__main__":
    main()
