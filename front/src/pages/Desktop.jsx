import { Box, Typography } from "@mui/material";
import Tabs from "@mui/material/Tabs";
import Tab from "@mui/material/Tab";
import { NavLink, useNavigate, useParams } from "react-router-dom";
import { useEffect, useLayoutEffect, useState } from "react";

import { Progress } from "../components/desktop/Progress";
import { Stationary } from "../components/desktop/Stationary";
import { DesktopOverview } from "../components/desktop/Overview";

const grayTextColor = "#aeb8b8";

export function Desktop() {
    const [value, setValue] = useState(0);

    const { topic } = useParams();
    const navigate = useNavigate();

    useLayoutEffect(() => {
        switch (topic) {
            case "overview":
                if (value !== 0) {
                    setValue(0);
                }
                return;
            case "stationary":
                if (value !== 1) {
                    setValue(1);
                }
                return;
            case "drinks":
                if (value !== 2) {
                    setValue(2);
                }
                return;
            case "tech":
                if (value !== 3) {
                    setValue(3);
                }
                return;
            default:
                if (value !== 0) {
                    setValue(0);
                }
                navigate("/desktop/overview");
                return;
        }
    }, [topic, value]);

    const handleChange = (_, newValue) => {
        setValue(newValue);
    };

    return (
        <>
            <Typography
                variant="h6"
                style={{
                    padding: "10px 10px 30px 30px",
                    textAlign: "center"
                }}
            >
                Рабочий стол
            </Typography>
            <Box sx={{ width: "100%", bgcolor: "background.paper" }}>
                <Tabs
                    value={value}
                    onChange={handleChange}
                    centered
                >
                    <Tab
                        label={
                            <NavLink to="/desktop/overview">
                                <div style={{ color: grayTextColor }}>
                                    Обзор
                                </div>
                            </NavLink>
                        }
                    />
                    <Tab
                        label={
                            <NavLink to="/desktop/stationary">
                                <div style={{ color: grayTextColor }}>
                                    Канцелярия
                                </div>
                            </NavLink>
                        }
                    />
                    <Tab
                        label={
                            <NavLink to="/desktop/drinks">
                                <div style={{ color: grayTextColor }}>
                                    Напитки
                                </div>
                            </NavLink>
                        }
                    />
                    <Tab
                        label={
                            <NavLink to="/desktop/tech">
                                <div style={{ color: grayTextColor }}>
                                    Техника
                                </div>
                            </NavLink>
                        }
                    />
                </Tabs>
            </Box>
            <div
                style={{
                    height: "30px",
                }}
            />
            {value === 0 ? (
                <>
                    <DesktopOverview />
                </>
            ) : value === 1 ? (
                <>
                    <Stationary />
                </>
            ) : (
                <>Техника</>
            )}
        </>
    );
}

export default function CenteredTabs() {
    const [value, setValue] = React.useState(0);

    const handleChange = (_, newValue) => {
        setValue(newValue);
    };

    return (
        <Box sx={{ width: "100%", bgcolor: "background.paper" }}>
            <Tabs
                value={value}
                onChange={handleChange}
                centered
            >
                <Tab label="Item One" />
                <Tab label="Item Two" />
                <Tab label="Item Three" />
            </Tabs>
        </Box>
    );
}
