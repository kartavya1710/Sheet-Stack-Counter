import streamlit as st
import cv2
import numpy as np
from PIL import Image

@st.cache_data
def preprocess_image(image_array):
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_image = clahe.apply(gray)
    blurred = cv2.GaussianBlur(clahe_image, (5, 5), 0)
    median = np.median(blurred)
    lower = int(max(0, (1.0 - 0.33) * median))
    upper = int(min(255, (1.0 + 0.33) * median))
    edges = cv2.Canny(blurred, lower, upper)
    return edges

def count_sheets_cv(edges):
    # Create a copy of edges to avoid modifying the cached object
    edges_copy = edges.copy()
    lines = cv2.HoughLinesP(edges_copy, 1, np.pi / 180, threshold=50, minLineLength=50, maxLineGap=10)
    
    if lines is None:
        return 0, edges_copy
    
    filtered_lines = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi
        if abs(angle) < 20:
            filtered_lines.append(line[0])
            cv2.line(edges_copy, (x1, y1), (x2, y2), (255, 0, 0), 1)
    
    sheet_count = len(filtered_lines)
    return sheet_count, edges_copy

def main():
    st.title("📊 Automated Sheet Stack Counter")
    
    st.markdown("""
    Welcome to the Automated Sheet Stack Counter! This application uses computer vision 
    techniques to estimate the number of sheets in a stack from an uploaded image.
    
    To get started, please upload an image of a sheet stack.
    """)

    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption='Uploaded Image', use_column_width=True)
        
        if st.button('Process Image', key='process'):
            with st.spinner('Processing...'):
                # Convert image to numpy array
                image_array = np.array(image.convert('RGB'))
                
                # Process the image
                edges = preprocess_image(image_array)
                cv_count, processed_edges = count_sheets_cv(edges)
                
                # Convert processed edges back to PIL format for display
                processed_image_pil = Image.fromarray(processed_edges)
                
                # Display results
                with col2:
                    st.image(processed_image_pil, caption='Processed Image', use_column_width=True)
                
                st.success(f"Estimated Number of Sheets: {cv_count}")
                
                # Visualization
                st.subheader("Visualization")
                st.bar_chart({"Sheet Count": [cv_count]})
                
                # Confidence metric (example)
                confidence = min(cv_count / 100, 1.0)  # Just an example, adjust as needed
                st.subheader("Confidence Metric")
                st.progress(confidence)
                st.text(f"Confidence: {confidence:.2%}")

    st.markdown("---")
    st.subheader("About")
    st.info(
        "This application uses computer vision to estimate the number of sheets in a stack. "
        "Simply upload an image, and the app will process it to detect the sheets automatically."
    )

if __name__ == "__main__":
    main()
    