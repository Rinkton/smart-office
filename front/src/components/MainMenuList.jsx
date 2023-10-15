import { List, ListItem, ListItemButton, ListItemText } from "@mui/material";
import { useState } from "react";

import OfficeMap from "../assets/icons/office_map.svg";
import Meetings from "../assets/icons/meetings.svg";
import Desktop from "../assets/icons/desktop.svg";
import Settings from "../assets/icons/settings.svg";
import { NavLink } from "react-router-dom";

export function MainMenuList() {
    const [list] = useState([
        {
            title: "Карта офиса",
            icon: OfficeMap,
            href: "/map",
        },
        {
            title: "Переговорные",
            icon: Meetings,
            href: "/rooms",
        },
        {
            title: "Рабочий стол",
            icon: Desktop,
            href: "/desktop",
        },
        {
            title: "Настройки",
            icon: Settings,
            href: "/settings",
        },
    ]);

    return (
        <List>
            {list.map(({ title, icon, href }, index) => (
                <ListItem
                    key={title}
                    disablePadding
                >
                    <NavLink
                        to={href}
                        style={{
                            textDecoration: "none",
                            color: "white",
                        }}
                    >
                        <ListItemButton
                            sx={{
                                display: "flex",
                                flexDirection: "row",
                                gap: "20px",
                            }}
                        >
                            <img
                                src={icon}
                                width={30}
                                height={30}
                                style={{
                                    fill: "white",
                                }}
                            />
                            <ListItemText primary={title} />
                        </ListItemButton>
                    </NavLink>
                </ListItem>
            ))}
        </List>
    );
}
