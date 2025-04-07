def polygon_area(poly):
    edge = [
        (poly[1][0] - poly[0][0]) * (poly[1][1] + poly[0][1]),
        (poly[2][0] - poly[1][0]) * (poly[2][1] + poly[1][1]),
        (poly[3][0] - poly[2][0]) * (poly[3][1] + poly[2][1]),
        (poly[0][0] - poly[3][0]) * (poly[0][1] + poly[3][1]),
    ]
    return np.sum(edge) / 2.0


def check_and_validate_polys(polys, tags, xxx_todo_changeme):
    (h, w) = xxx_todo_changeme

    if polys.shape[0] == 0:
        return polys

    polys[:, :, 0] = np.clip(polys[:, :, 0], 0, w - 1)
    polys[:, :, 1] = np.clip(polys[:, :, 1], 0, h - 1)

    validated_polys = []
    validated_tags = []

    for poly, tag in zip(polys, tags):
        p_area = polygon_area(poly)

        if abs(p_area) < 1:
            print("invalid poly")
            continue
        if p_area > 0:
            print("poly in wrong direction")
            poly = poly[(0, 3, 2, 1), :]
        validated_polys.append(poly)
        validated_tags.append(tag)

    return np.array(validated_polys), np.array(validated_tags)


def crop_area(im, polys, tags, crop_background=False, max_tries=50):
    h, w, _ = im.shape
    pad_h = h // 10
    pad_w = w // 10
    h_array = np.zeros((h + pad_h * 2), dtype=np.int32)
    w_array = np.zeros((w + pad_w * 2), dtype=np.int32)

    for poly in polys:
        poly = np.round(poly, decimals=0).astype(np.int32)
        minx = np.min(poly[:, 0])
        maxx = np.max(poly[:, 0])
        w_array[minx + pad_w : maxx + pad_w] = 1
        miny = np.min(poly[:, 1])
        maxy = np.max(poly[:, 1])
        h_array[miny + pad_h : maxy + pad_h] = 1

    h_axis = np.where(h_array == 0)[0]
    w_axis = np.where(w_array == 0)[0]

    if len(h_axis) == 0 or len(w_axis) == 0:
        return im, polys, tags

    for i in range(max_tries):
        xx = np.random.choice(w_axis, size=2)
        xmin = np.min(xx) - pad_w
        xmax = np.max(xx) - pad_w
        xmin = np.clip(xmin, 0, w - 1)
        xmax = np.clip(xmax, 0, w - 1)
        yy = np.random.choice(h_axis, size=2)
        ymin = np.min(yy) - pad_h
        ymax = np.max(yy) - pad_h
        ymin = np.clip(ymin, 0, h - 1)
        ymax = np.clip(ymax, 0, h - 1)

        if (
            xmax - xmin < cfg.min_crop_side_ratio * w
            or ymax - ymin < cfg.min_crop_side_ratio * h
        ):
            continue
        
        if polys.shape[0] != 0:
            poly_axis_in_area = (
                (polys[:, :, 0] >= xmin)
                & (polys[:, :, 0] <= xmax)
                & (polys[:, :, 1] >= ymin)
                & (polys[:, :, 1] <= ymax)
            )
            selected_polys = np.where(np.sum(poly_axis_in_area, axis=1) == 4)[0]
        else:
            selected_polys = []
        
        if len(selected_polys) == 0:
            if crop_background:
                return (
                    im[ymin : ymax + 1, xmin : xmax + 1, :],
                    polys[selected_polys],
                    tags[selected_polys],
                )
            else:
                continue
        
        im = im[ymin : ymax + 1, xmin : xmax + 1, :]
        polys = polys[selected_polys]
        tags = tags[selected_polys]
        polys[:, :, 0] -= xmin
        polys[:, :, 1] -= ymin

        return im, polys, tags

    return im, polys, tags


def shrink_poly(poly, r):
    R = 0.3

    if np.linalg.norm(poly[0] - poly[1]) + np.linalg.norm(poly[2] - poly[3]) > np.linalg.norm(poly[0] - poly[3]) + np.linalg.norm(poly[1] - poly[2]):

        ## p0, p1
        theta = np.arctan2((poly[1][1] - poly[0][1]), (poly[1][0] - poly[0][0]))
        poly[0][0] += R * r[0] * np.cos(theta)
        poly[0][1] += R * r[0] * np.sin(theta)
        poly[1][0] -= R * r[1] * np.cos(theta)
        poly[1][1] -= R * r[1] * np.sin(theta)

        ## p2, p3
        theta = np.arctan2((poly[2][1] - poly[3][1]), (poly[2][0] - poly[3][0]))
        poly[3][0] += R * r[3] * np.cos(theta)
        poly[3][1] += R * r[3] * np.sin(theta)
        poly[2][0] -= R * r[2] * np.cos(theta)
        poly[2][1] -= R * r[2] * np.sin(theta)

        ## p0, p3
        theta = np.arctan2((poly[3][0] - poly[0][0]), (poly[3][1] - poly[0][1]))
        poly[0][0] += R * r[0] * np.sin(theta)
        poly[0][1] += R * r[0] * np.cos(theta)
        poly[3][0] -= R * r[3] * np.sin(theta)
        poly[3][1] -= R * r[3] * np.cos(theta)

        ## p1, p2
        theta = np.arctan2((poly[2][0] - poly[1][0]), (poly[2][1] - poly[1][1]))
        poly[1][0] += R * r[1] * np.sin(theta)
        poly[1][1] += R * r[1] * np.cos(theta)
        poly[2][0] -= R * r[2] * np.sin(theta)
        poly[2][1] -= R * r[2] * np.cos(theta)

    else:

        ## p0, p3
        theta = np.arctan2((poly[3][0] - poly[0][0]), (poly[3][1] - poly[0][1]))
        poly[0][0] += R * r[0] * np.sin(theta)
        poly[0][1] += R * r[0] * np.cos(theta)
        poly[3][0] -= R * r[3] * np.sin(theta)
        poly[3][1] -= R * r[3] * np.cos(theta)

        ## p1, p2
        theta = np.arctan2((poly[2][0] - poly[1][0]), (poly[2][1] - poly[1][1]))
        poly[1][0] += R * r[1] * np.sin(theta)
        poly[1][1] += R * r[1] * np.cos(theta)
        poly[2][0] -= R * r[2] * np.sin(theta)
        poly[2][1] -= R * r[2] * np.cos(theta)

        ## p0, p1
        theta = np.arctan2((poly[1][1] - poly[0][1]), (poly[1][0] - poly[0][0]))
        poly[0][0] += R * r[0] * np.cos(theta)
        poly[0][1] += R * r[0] * np.sin(theta)
        poly[1][0] -= R * r[1] * np.cos(theta)
        poly[1][1] -= R * r[1] * np.sin(theta)

        ## p2, p3
        theta = np.arctan2((poly[2][1] - poly[3][1]), (poly[2][0] - poly[3][0]))
        poly[3][0] += R * r[3] * np.cos(theta)
        poly[3][1] += R * r[3] * np.sin(theta)
        poly[2][0] -= R * r[2] * np.cos(theta)
        poly[2][1] -= R * r[2] * np.sin(theta)

    return poly


def point_dist_to_line(p1, p2, p3):
    x = np.linalg.norm(np.cross(p2 - p1, p1 - p3)) / np.linalg.norm(p2 - p1)
    return x


def fit_line(p1, p2):
    if p1[0] == p1[1]:
        return [1.0, 0.0, -p1[0]]
    else:
        [k, b] = np.polyfit(p1, p2, deg=1)
        return [k, -1.0, b]


def line_cross_point(line1, line2):
    if line1[0] != 0 and line1[0] == line2[0]:
        print("Cross point does not exist")
        return None
    
    if line1[0] == 0 and line2[0] == 0:
        print("Cross point does not exist")
        return None
    
    if line1[1] == 0:
        x = -line1[2]
        y = line2[0] * x + line2[2]
    elif line2[1] == 0:
        x = -line2[2]
        y = line1[0] * x + line1[2]
    else:
        k1, _, b1 = line1
        k2, _, b2 = line2
        x = -(b1 - b2) / (k1 - k2)
        y = k1 * x + b1
    
    return np.array([x, y], dtype=np.float32)


def line_vertical(line, point):
    if line[1] == 0:
        vertical = [0, -1, point[1]]
    else:
        if line[0] == 0:
            vertical = [1, 0, -point[0]]
        else:
            vertical = [-1.0 / line[0], -1, point[1] - (-1 / line[0] * point[0])]
    return vertical


def rectangle_from_parallelogram(poly):
    p0, p1, p2, p3 = poly
    angle_p0 = np.arccos(
        np.dot(p1 - p0, p3 - p0) / (np.linalg.norm(p0 - p1) * np.linalg.norm(p3 - p0))
    )

    if angle_p0 < 0.5 * np.pi:
        if np.linalg.norm(p0 - p1) > np.linalg.norm(p0 - p3):

            ## p0
            p2p3 = fit_line([p2[0], p3[0]], [p2[1], p3[1]])
            p2p3_vertical = line_vertical(p2p3, p0)
            new_p3 = line_cross_point(p2p3, p2p3_vertical)

            ## p2
            p0p1 = fit_line([p0[0], p1[0]], [p0[1], p1[1]])
            p0p1_vertical = line_vertical(p0p1, p2)
            new_p1 = line_cross_point(p0p1, p0p1_vertical)

            return np.array([p0, new_p1, p2, new_p3], dtype=np.float32)
        else:
            p1p2 = fit_line([p1[0], p2[0]], [p1[1], p2[1]])
            p1p2_vertical = line_vertical(p1p2, p0)
            new_p1 = line_cross_point(p1p2, p1p2_vertical)
            p0p3 = fit_line([p0[0], p3[0]], [p0[1], p3[1]])
            p0p3_vertical = line_vertical(p0p3, p2)
            new_p3 = line_cross_point(p0p3, p0p3_vertical)

            return np.array([p0, new_p1, p2, new_p3], dtype=np.float32)
    else:
        if np.linalg.norm(p0 - p1) > np.linalg.norm(p0 - p3):

            ## p1
            p2p3 = fit_line([p2[0], p3[0]], [p2[1], p3[1]])
            p2p3_vertical = line_vertical(p2p3, p1)
            new_p2 = line_cross_point(p2p3, p2p3_vertical)

            ## p3
            p0p1 = fit_line([p0[0], p1[0]], [p0[1], p1[1]])
            p0p1_vertical = line_vertical(p0p1, p3)
            new_p0 = line_cross_point(p0p1, p0p1_vertical)

            return np.array([new_p0, p1, new_p2, p3], dtype=np.float32)
        else:
            p0p3 = fit_line([p0[0], p3[0]], [p0[1], p3[1]])
            p0p3_vertical = line_vertical(p0p3, p1)
            new_p0 = line_cross_point(p0p3, p0p3_vertical)
            p1p2 = fit_line([p1[0], p2[0]], [p1[1], p2[1]])
            p1p2_vertical = line_vertical(p1p2, p3)
            new_p2 = line_cross_point(p1p2, p1p2_vertical)

            return np.array([new_p0, p1, new_p2, p3], dtype=np.float32)


def sort_rectangle(poly):
    p_lowest = np.argmax(poly[:, 1])

    if np.count_nonzero(poly[:, 1] == poly[p_lowest, 1]) == 2:
        p0_index = np.argmin(np.sum(poly, axis=1))
        p1_index = (p0_index + 1) % 4
        p2_index = (p0_index + 2) % 4
        p3_index = (p0_index + 3) % 4

        return poly[[p0_index, p1_index, p2_index, p3_index]], 0.0
    else:
        p_lowest_right = (p_lowest - 1) % 4
        p_lowest_left = (p_lowest + 1) % 4

        angle = np.arctan(
            -(poly[p_lowest][1] - poly[p_lowest_right][1])
            / (poly[p_lowest][0] - poly[p_lowest_right][0])
        )

        if angle <= 0:
            print(angle, poly[p_lowest], poly[p_lowest_right])

            if angle / np.pi * 180 > 45:
                p2_index = p_lowest
                p1_index = (p2_index - 1) % 4
                p0_index = (p2_index - 2) % 4
                p3_index = (p2_index + 1) % 4
                return poly[[p0_index, p1_index, p2_index, p3_index]], -(np.pi / 2 - angle)
            else:
                p3_index = p_lowest
                p0_index = (p3_index + 1) % 4
                p1_index = (p3_index + 2) % 4
                p2_index = (p3_index + 3) % 4
                return poly[[p0_index, p1_index, p2_index, p3_index]], angle


def restore_rectangle_rbox(origin, geometry):
    d = geometry[:, :4]
    angle = geometry[:, 4]
    origin_0 = origin[angle >= 0]
    d_0 = d[angle >= 0]
    angle_0 = angle[angle >= 0]

    if origin_0.shape[0] > 0:
        p = np.array(
            [
                np.zeros(d_0.shape[0]),
                -d_0[:, 0] - d_0[:, 2],
                d_0[:, 1] + d_0[:, 3],
                -d_0[:, 0] - d_0[:, 2],
                d_0[:, 1] + d_0[:, 3],
                np.zeros(d_0.shape[0]),
                np.zeros(d_0.shape[0]),
                np.zeros(d_0.shape[0]),
                d_0[:, 3],
                -d_0[:, 2],
            ]
        )
        
        p = p.transpose((1, 0)).reshape((-1, 5, 2))  # N*5*2
        rotate_matrix_x = np.array([np.cos(angle_0), np.sin(angle_0)]).transpose((1, 0))
        rotate_matrix_x = (
            np.repeat(rotate_matrix_x, 5, axis=1)
            .reshape(-1, 2, 5)
            .transpose((0, 2, 1))
        )  # N*5*2
        rotate_matrix_y = np.array([-np.sin(angle_0), np.cos(angle_0)]).transpose((1, 0))
        rotate_matrix_y = (
            np.repeat(rotate_matrix_y, 5, axis=1)
            .reshape(-1, 2, 5)
            .transpose((0, 2, 1))
        )
        p_rotate_x = np.sum(rotate_matrix_x * p, axis=2)[:, :, np.newaxis]  # N*5*1
        p_rotate_y = np.sum(rotate_matrix_y * p, axis=2)[:, :, np.newaxis]  # N*5*1
        p_rotate = np.concatenate([p_rotate_x, p_rotate_y], axis=2)  # N*5*2
        p3_in_origin = origin_0 - p_rotate[:, 4, :]
        new_p0 = p_rotate[:, 0, :] + p3_in_origin  # N*2
        new_p1 = p_rotate[:, 1, :] + p3_in_origin
        new_p2 = p_rotate[:, 2, :] + p3_in_origin
        new_p3 = p_rotate[:, 3, :] + p3_in_origin
        new_p_0 = np.concatenate(
            [
                new_p0[:, np.newaxis, :],
                new_p1[:, np.newaxis, :],
                new_p2[:, np.newaxis, :],
                new_p3[:, np.newaxis, :],
            ],
            axis=1,
        )  # N*4*2
    else:
        new_p_0 = np.zeros((0, 4, 2))
    
    origin_1 = origin[angle < 0]
    d_1 = d[angle < 0]
    angle_1 = angle[angle < 0]

    if origin_1.shape[0] > 0:
        p = np.array(
            [
                -d_1[:, 1] - d_1[:, 3],
                -d_1[:, 0] - d_1[:, 2],
                np.zeros(d_1.shape[0]),
                -d_1[:, 0] - d_1[:, 2],
                np.zeros(d_1.shape[0]),
                np.zeros(d_1.shape[0]),
                -d_1[:, 1] - d_1[:, 3],
                np.zeros(d_1.shape[0]),
                -d_1[:, 1],
                -d_1[:, 2],
            ]
        )
        p = p.transpose((1, 0)).reshape((-1, 5, 2))  # N*5*2
        rotate_matrix_x = np.array([np.cos(-angle_1), -np.sin(-angle_1)]).transpose((1, 0))
        rotate_matrix_x = (
            np.repeat(rotate_matrix_x, 5, axis=1)
            .reshape(-1, 2, 5)
            .transpose((0, 2, 1))
        )  # N*5*2
        rotate_matrix_y = np.array([np.sin(-angle_1), np.cos(-angle_1)]).transpose((1, 0))
        rotate_matrix_y = (
            np.repeat(rotate_matrix_y, 5, axis=1)
            .reshape(-1, 2, 5)
            .transpose((0, 2, 1))
        )
        p_rotate_x = np.sum(rotate_matrix_x * p, axis=2)[:, :, np.newaxis]  # N*5*1
        p_rotate_y = np.sum(rotate_matrix_y * p, axis=2)[:, :, np.newaxis]  # N*5*1
        p_rotate = np.concatenate([p_rotate_x, p_rotate_y], axis=2)  # N*5*2
        p3_in_origin = origin_1 - p_rotate[:, 4, :]
        new_p0 = p_rotate[:, 0, :] + p3_in_origin  # N*2
        new_p1 = p_rotate[:, 1, :] + p3_in_origin
        new_p2 = p_rotate[:, 2, :] + p3_in_origin
        new_p3 = p_rotate[:, 3, :] + p3_in_origin
        new_p_1 = np.concatenate(
            [
                new_p0[:, np.newaxis, :],
                new_p1[:, np.newaxis, :],
                new_p2[:, np.newaxis, :],
                new_p3[:, np.newaxis, :],
            ],
            axis=1,
        )  # N*4*2
    else:
        new_p_1 = np.zeros((0, 4, 2))
    
    return np.concatenate([new_p_0, new_p_1])


def generate_rbox(im_size, polys, tags):
    h, w = im_size
    poly_mask = np.zeros((h, w), dtype=np.uint8)
    score_map = np.zeros((h, w), dtype=np.uint8)
    geo_map = np.zeros((h, w, 5), dtype=np.float32)
    training_mask = np.ones((h, w), dtype=np.uint8)

    for poly_idx, poly_tag in enumerate(zip(polys, tags)):
        poly = poly_tag[0]
        tag = poly_tag[1]
        r = [None, None, None, None]

        for i in range(4):
            r[i] = min(
                np.linalg.norm(poly[i] - poly[(i + 1) % 4]),
                np.linalg.norm(poly[i] - poly[(i - 1) % 4]),
            )
        
        shrunk_poly = shrink_poly(poly.copy(), r).astype(np.int32)[np.newaxis, :, :]
        cv2.fillPoly(score_map, shrunk_poly, 1)
        cv2.fillPoly(poly_mask, shrunk_poly, poly_idx + 1)
        poly_h = min(
            np.linalg.norm(poly[0] - poly[3]), np.linalg.norm(poly[1] - poly[2])
        )
        poly_w = min(
            np.linalg.norm(poly[0] - poly[1]), np.linalg.norm(poly[2] - poly[3])
        )

        if min(poly_h, poly_w) < cfg.min_text_size:
            cv2.fillPoly(training_mask, poly.astype(np.int32)[np.newaxis, :, :], 0)
        if tag:
            cv2.fillPoly(training_mask, poly.astype(np.int32)[np.newaxis, :, :], 0)
        
        xy_in_poly = np.argwhere(poly_mask == (poly_idx + 1))
        box = cv2.minAreaRect(poly)
        (p0_rect, p1_rect, p2_rect, p3_rect), angle = sort_rectangle(cv2.boxPoints(box))

        for y, x in xy_in_poly:
            point = np.array([x, y], dtype=np.float32)
            geo_map[y, x, 0] = point_dist_to_line(p0_rect, p1_rect, point)
            geo_map[y, x, 1] = point_dist_to_line(p1_rect, p2_rect, point)
            geo_map[y, x, 2] = point_dist_to_line(p2_rect, p3_rect, point)
            geo_map[y, x, 3] = point_dist_to_line(p3_rect, p0_rect, point)
            geo_map[y, x, 4] = angle
        
    return score_map, geo_map, training_mask


def infer_and_test(model):
    output_path = infer.infer(model, validation_dataset=True)
    zip_path = "tmp_results.zip"

    with ZipFile(zip_path, "w") as zipObj:
        for fn in os.listdir(output_path):
            if not ".txt" in fn:
                continue
            zipObj.write(os.path.join(output_path, fn), fn)
    res_dic = script.main(zip_path)
    
    return res_dic["method"]
