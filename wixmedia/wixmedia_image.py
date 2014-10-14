from .exceptions import WixMediaCmdNotAllowed


class WixMediaImage(object):
    COMMAND_NONE   = ""
    COMMAND_SRZ    = "srz"
    COMMAND_SRB    = "srb"
    COMMAND_CANVAS = "canvas"
    COMMAND_FILL   = "fill"
    COMMAND_CROP   = "crop"

    def __init__(self, file_uri, org_name):
        self.transform_command = None
        self.transform_params  = None
        self.adjustment_params = None
        self.filter_params     = None

        self.file_uri          = file_uri
        self.org_name          = org_name

        self.reset()

    def reset(self):
        self.transform_command = WixMediaImage.COMMAND_NONE
        self.transform_params  = {}
        self.adjustment_params = {}
        self.filter_params     = {}

    def srz(self, width, height, quality=85, alignment=1, radius=0.5, amount=0.2, threshold=0.0):

        if self.transform_command != WixMediaImage.COMMAND_NONE:
            raise WixMediaCmdNotAllowed("Command already set: %s. Reset image before applying command." % self.transform_command)

        self.transform_command = WixMediaImage.COMMAND_SRZ

        self.transform_params = {
            "width":     width,
            "height":    height,
            "quality":   quality,
            "alignment": alignment,
            "radius":    radius,
            "amount":    amount,
            "threshold": threshold
        }

        return self

    def srb(self, width, height, quality=85, radius=0.5, amount=0.2, threshold=0.0):

        if self.transform_command != WixMediaImage.COMMAND_NONE:
            raise WixMediaCmdNotAllowed("Command already set: %s. Reset image before applying command." % self.transform_command)

        self.transform_command = WixMediaImage.COMMAND_SRB

        self.transform_params = {
            "width":     width,
            "height":    height,
            "quality":   quality,
            "radius":    radius,
            "amount":    amount,
            "threshold": threshold
        }

        return self

    def canvas(self, width, height, quality=85, alignment=1):

        if self.transform_command != WixMediaImage.COMMAND_NONE:
            raise WixMediaCmdNotAllowed("Command already set: %s. Reset image before applying command." % self.transform_command)

        self.transform_command = WixMediaImage.COMMAND_CANVAS

        self.transform_params = {
            "width":     width,
            "height":    height,
            "quality":   quality,
            "alignment": alignment
        }

        return self

    def crop(self, x, y, width, height, quality=85):

        if self.transform_command != WixMediaImage.COMMAND_NONE:
            raise WixMediaCmdNotAllowed("Command already set: %s. Reset image before applying command." % self.transform_command)

        self.transform_command = WixMediaImage.COMMAND_CROP

        self.transform_params = {
            "width":   width,
            "height":  height,
            "quality": quality,
            "x":       x,
            "y":       y
        }

        return self

    def fill(self, width, height, quality=85):

        if self.transform_command != WixMediaImage.COMMAND_NONE:
            raise WixMediaCmdNotAllowed("Command already set: %s. Reset image before applying command." % self.transform_command)

        self.transform_command = WixMediaImage.COMMAND_FILL

        self.transform_params = {
            "width":   width,
            "height":  height,
            "quality": quality
        }

        return self

    def adjust(self, *props_list, **props_dict):

        self.adjustment_params.update({p: True for p in props_list})
        self.adjustment_params.update(props_dict)

        return self

    def filter(self, *funcs_list, **funcs_dict):

        self.filter_params.update({f: True for f in funcs_list})
        self.filter_params.update(funcs_dict)

        return self

    def get_rest_url(self):

        params = [self.file_uri]

        if self.transform_command != WixMediaImage.COMMAND_NONE:
            params.extend(
                [self.transform_command,
                 ",".join(["%s_%s" % (key, val) for key, val in self.transform_params.iteritems()])]
            )

        if self.adjustment_params:
            params.extend(
                ["adjust",
                 ",".join(["%s_%s" % (key, val) if val is not True else key
                           for key, val in self.adjustment_params.iteritems()])]
            )

        if self.filter_params:
            params.extend(
                ["filter",
                 ",".join(["%s_%s" % (key, val) if val is not True else key
                          for key, val in self.filter_params.iteritems()])]
            )

        params.append(self.org_name)

        url = "/".join(params)

        return url

    def get_img_tag(self, **kwargs):
        img_params = ''.join([' %s="%s"' % (name, value) for name, value in kwargs.iteritems()])

        return '<img src="%s"%s>' % (self.get_rest_url(), img_params)
    
    def __str__(self):
        return "<WixMediaImage %s (%s ), command=%s [%s]>" % (
            self.file_uri, self.org_name, self.transform_command, self.transform_params
        )
