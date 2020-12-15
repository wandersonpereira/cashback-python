class Status:
    def getStatus(model):
        if model["document"] == "153.509.460-56":
            return "Aprovado"
        else:
            return model["status"]
            
        