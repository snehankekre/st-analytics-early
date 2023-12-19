import streamlit as st


@st.experimental_singleton
def init_analytics():
    import os

    index_filename = os.path.join(os.path.dirname(st.__file__), "static", "index.html")
    # Read in the file
    with open(index_filename, "r") as f:
        data = f.read()

    if not "gtag.js" in data:
        tracking_code = """\n\t<!-- Google tag (gtag.js) -->\n\t<script async src="https://www.googletagmanager.com/gtag/js?id=G-8DX64VZSF6"></script>\n\t<script>window.dataLayer = window.dataLayer || [];function gtag() { dataLayer.push(arguments); }gtag('js', new Date());gtag('config', 'G-8DX64VZSF6');</script>\n"""
        data = data.replace("<head>", "<head>" + tracking_code)

        with open(index_filename, "w") as f:
            f.write(data)


init_analytics()

st.header("Streamlit App")


def analytics():
    st.components.v1.html(
        """
        <script>
        window.parent.gtag('event', 'button_click', {action: 'click'});
        </script>
        """,
        height=0,
    )


if st.button("Fire event", key="button1", on_click=analytics):
    st.write("Event fired")

check = st.checkbox("Other button", key="button2")
st.text("Checkbox value:%s" % check)
st.components.v1.html(
    """
    <script>
    window.parent.gtag('event', 'checkbox', {action: 'check', value: '%s'});
    </script>
    """
    % check,
    height=0,
)

upload = st.file_uploader("Upload a file", key="button3")
if upload is not None:
    st.write("File uploaded")
    st.components.v1.html(
        """
        <script>
        window.parent.gtag('event', 'upload', {action: 'upload', value: '%s'});
        </script>
        """
        % upload.name,
        height=0,
    )

# Track a slider value as it changes with gtag
val = st.slider("Slide me", 0, 100)
st.components.v1.html(
    """
    <script>
    window.parent.gtag('event', 'slide', {action: 'slide', value: %d});
    </script>
    """
    % val,
    height=0,
)
