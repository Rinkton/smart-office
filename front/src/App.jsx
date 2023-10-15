import { ThemeProvider, createTheme } from "@mui/material/styles";
import { MenuLayout } from "./components/MenuLayout";
import { Box } from "@mui/material";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import { Desktop } from "./pages/Desktop";
import { MeetingRooms } from "./pages/Rooms";
import { Settings } from "./pages/Settings";
import { OfficeMap } from "./pages/OfficeMap";

const darkTheme = createTheme({
    palette: {
        mode: "dark",
    },
});

export default function App() {
    return (
        <BrowserRouter>
            <ThemeProvider theme={darkTheme}>
                <Box
                    sx={{
                        width: "100vw",
                        display: "flex",
                        flexDirection: "column",
                        justifyContent: "start",
                        minHeight: "100vh",
                    }}
                >
                    <MenuLayout>
                        <Routes>
                            <Route
                                path="/map"
                                element={<OfficeMap />}
                            />

                            <Route
                                path="/rooms"
                                element={<MeetingRooms />}
                            />
                            <Route
                                path="/rooms/:room_id"
                                element={<MeetingRooms />}
                            />

                            <Route
                                path="/desktop"
                                element={<Desktop />}
                            />
                            <Route
                                path="/desktop/:topic"
                                element={<Desktop />}
                            />

                            <Route
                                path="/settings"
                                element={<Settings />}
                            />
                        </Routes>
                    </MenuLayout>
                </Box>
            </ThemeProvider>
        </BrowserRouter>
    );
}
