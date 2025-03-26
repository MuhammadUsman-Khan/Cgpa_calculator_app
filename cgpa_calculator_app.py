import streamlit as st

def get_grade_point(percentage):
    if percentage >= 91:
        return 4.0
    elif percentage >= 80:
        return 3.7
    elif percentage >= 75:
        return 3.3
    elif percentage >= 71:
        return 3.0
    elif percentage >= 68:
        return 2.7
    elif percentage >= 64:
        return 2.3
    elif percentage >= 61:
        return 2.0
    elif percentage >= 58:
        return 1.7
    elif percentage >= 54:
        return 1.3
    elif percentage >= 50:
        return 1.0
    else:
        return 0.0
  
def calculate_cgpa():
    st.title("CGPA Calculator")
    total_point = 0
    total_credit = 0

    num_subjects = st.number_input("Enter the number of courses or subjects:", min_value=1, step=1, key="num_subjects")

    for i in range(1, num_subjects + 1):
        st.subheader(f"Subject {i}:")
        obtained_marks = st.number_input(f"Obtained marks for Subject {i}:", min_value=0.0, step=0.5, format="%.1f", key=f"obt_{i}")
        total_marks = st.number_input(f"Total marks for Subject {i}:", min_value=0.1, step=0.5, format="%.1f", key=f"total_{i}")
        credit_hours = st.number_input(f"Credit hours for Subject {i}:", min_value=1, step=1, key=f"credit_{i}")

        percentage = (obtained_marks / total_marks) * 100
        grade_points = get_grade_point(percentage)
        total_point += grade_points * credit_hours
        total_credit += credit_hours

    if st.button("Calculate CGPA"):
        if total_credit == 0:
            st.error("No subjects entered or invalid entries.")
        else:
            cgpa = total_point / total_credit
            st.success(f"Your CGPA is {cgpa:.2f}")
    st.markdown("---")
    st.markdown("<h3 style='text-align: center;'>🎓 Made by Muhammad Usman Khan 🎓</h3>", unsafe_allow_html=True)


def main():
    calculate_cgpa()

if __name__ == "__main__":
    main()
