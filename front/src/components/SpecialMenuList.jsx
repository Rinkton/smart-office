import { List, ListItem, ListItemButton, ListItemText } from "@mui/material";
import { useState } from "react";

import User from "../assets/icons/user.svg";
import Support from "../assets/icons/support.svg";

export function SpecialMenuList() {
    const [list] = useState([
        {
            title: "id: #1258",
            icon: User,
        },
        {
            title: "Техподдержка",
            icon: Support,
        },
    ]);

    return (
        <List
            sx={{
                display: "flex",
                flexDirection: "row",
                justifyContent: "center",
                gap: "10px",
            }}
        >
            {list.map(({ title, icon }, index) => (
                <ListItem
                    key={title}
                    disablePadding
                    sx={{
                        borderRadius: "50%",
                        width: "80px",
                    }}
                >
                    <ListItemButton
                        sx={{
                            display: "flex",
                            flexDirection: "column",
                            gap: "8px",
                        }}
                    >
                        <img
                            src={icon}
                            width={20}
                            height={20}
                            style={{
                                fill: "white",
                            }}
                        />
                        <ListItemText
                            primaryTypographyProps={{
                                fontSize: "10px",
                            }}
                            primary={title}
                        />
                    </ListItemButton>
                </ListItem>
            ))}
        </List>
    );
}
