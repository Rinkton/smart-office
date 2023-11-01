import * as React from "react";
import Card from "@mui/material/Card";
import CardActions from "@mui/material/CardActions";
import CardContent from "@mui/material/CardContent";
import CardMedia from "@mui/material/CardMedia";
import Button from "@mui/material/Button";
import Typography from "@mui/material/Typography";

export function RoomCard({ img, alt, title, description, room_id, setOpenDialog }) {

    return (
        <Card
            sx={{
                display: "flex",
                flexDirection: "row",
                maxWidth: "900px",
            }}
        >
            <CardMedia
                sx={{ minWidth: 200, width: 200 }}
                image={img}
                title={alt}
            />
            <CardContent
                sx={{
                    flexGrow: 1,
                }}
            >
                <Typography
                    gutterBottom
                    variant="h5"
                    component="div"
                >
                    {title}
                </Typography>
                <Typography
                    variant="body2"
                    color="text.secondary"
                >
                    {description}
                </Typography>
            </CardContent>
            <CardActions
                sx={{
                    display: "flex",
                    flexDirection: "column",
                    alignItems: "center",
                    justifyContent: "center",
                }}
            >
                <Button
                    size="small"
                    color="success"
                    onClick={() => setOpenDialog(room_id)}
                >
                    Забронировать
                </Button>
                <Button
                    size="small"
                    color="primary"
                >
                    Подробнее
                </Button>
            </CardActions>
        </Card>
    );
}
