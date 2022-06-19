import Container from "@mui/material/Container";
import "./App.css";
import NavBar from "./components/NavBar/NavBar";

function App() {
  return (
    <Container
      sx={{
        padding: "0",
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
      }}
    >
      Hello
      <NavBar />
    </Container>
  );
}

export default App;
