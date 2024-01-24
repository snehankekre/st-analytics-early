
import streamlit as st


def track_button():
    st.components.v1.html(
        """
        <script>
        window.parent.gtag('event', 'button_click', {action: 'click'});
        </script>
        """,
        height=0,
        width=0,
    )
    st.components.v1.html(
        """
        <script>
        window.parent.mixpanel.track('Button click', {
            'Action': 'click'
        });
        </script>
        """,
        height=0,
        width=0,
    )


if st.button("Fire event", key="button1", on_click=track_button):
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
        width=0,
    )
    st.components.v1.html(
        """
        <script>
        window.parent.mixpanel.track('File upload', {'filename': '%s'});
        </script>
        """
        % upload.name,
        height=0,
        width=0,
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
